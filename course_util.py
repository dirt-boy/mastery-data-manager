"""Main logic file. Manages data pipeline."""
from gAPI import Create_Service
import ast
import json
import os
import sys

sys.path.insert(1, 'logging-test')
import extract_data as RUBRIC
import js2py
import makelogger as logger

js2py.translate_file('course_util.js', 'course_utiljs.py')
import find_except as exc
import to_csv as csv

from concurrent.futures import (
    as_completed,
    ThreadPoolExecutor
)
from course_utiljs import course_utiljs


GCLOGGER = logger.get_logger(__name__)
RUBRIC_REGEX_KEYS = RUBRIC.regex_gen(0)
SUBMISSION_REGEX_KEYS = RUBRIC.regex_gen(1)


CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses https://www.googleapis.com/auth/classroom.rosters https://www.googleapis.com/auth/classroom.profile.emails https://www.googleapis.com/auth/classroom.rosters']

COURSE_FIELDS = ''
TEACHER_FIELDS = ['teachers/courseId','teachers/userId','teachers/profile']
STUDENT_FIELDS = ['students/courseId','students/userId','students/profile']
COURSEWORK_FIELDS = ['courseWork/id','courseWork/title','courseWork/maxPoints','courseWork/description','courseWork/creationTime','courseWork/alternateLink','courseWork/courseId']
SUBMISSION_FIELDS = ['studentSubmissions/id','studentSubmissions/assignedGrade','studentSubmissions/alternateLink','studentSubmissions/courseWorkId','studentSubmissions/courseId','studentSubmissions/userId','studentSubmissions/state']


def writefile(name, content):
    save_path = os.path.abspath("logs")
    completename = os.path.join(save_path, str(name))
    with open(completename+".json", "w") as f:
        f.write(content)

def write_submissions(submissions, filename_suffix=''):
    # Save submission JSON blob to `submissions.json`
    string = json.dumps(submissions, sort_keys=True, indent=4)
    writefile('submissions' + filename_suffix, string)
    csv.fullconvert()

def log_all(results):
    for res, l in enumerate(results):
        GCLOGGER.info(res)

def format_all(results):
    return course_utiljs.formatAll(results)


class CourseFetcher:

    def __init__(self, classroom=None):
        self.classroom = classroom or Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

        #testing write to file before logging. commenting out logs
        self.test_list = []
        self.sub_list = []

        # Batch requests based on which callback we'll handle them with
        self.course_batch = self.classroom.new_batch_http_request(callback=self.handle_courses)
        self.course_prop_batch = self.classroom.new_batch_http_request(callback=self.handle_course_props)
        self.submission_batch = self.classroom.new_batch_http_request(callback=self.handle_submissions)

        # Basic info about courses
        self.ref_d = {}

    def handle_courses(self, request_id, response, exception):
        """Callback for when we've received the list of courses."""
        if exception is not None:
            #GCLOGGER.info(exception)
            print(exception)
        else:
            #GCLOGGER.info(response)

            # Store all responses in `test_list`
            if not os.path.exists(str(request_id)+".json"):
                self.test_list.append(response)
                #writefile(str(request_id), str(response))

            # Fetch coursework, teachers, and students for each course
            for i, c in enumerate(response['courses']):
                self.course_prop_batch.add(
                    self.classroom.courses().courseWork().list(
                        courseId=c['id'],
                        fields=','.join(COURSEWORK_FIELDS)
                    )
                )

                self.course_prop_batch.add(
                    self.classroom.courses().teachers().list(
                        courseId=c['id'],
                        fields=','.join(TEACHER_FIELDS)
                    )
                )

                self.course_prop_batch.add(
                    self.classroom.courses().students().list(
                        courseId=c['id'],
                        fields=','.join(STUDENT_FIELDS)
                    )
                )

    def handle_course_props(self, request_id, response, exception):
        """Callback for when we've received lists of coursework, students, or teachers."""
        if exception is not None:
            #GCLOGGER.info(exception)
            print(exception)
        else:
            #GCLOGGER.info(response)
            #print(response)

            # Store all responses in `test_list`
            if not os.path.exists(str(request_id)+".json"):
                self.test_list.append(response)
                #writefile(str(request_id), str(response))

            # Fetch submissions for each piece of coursework
            if 'courseWork' in response:
                for i, cw in enumerate(response['courseWork']):
                    if ('Project' in cw['title'] and 'Ticket' not in cw['title'] and 'Do Now' not in cw['title'] and 'Slides' not in cw['title'] and 'Day' not in cw['title']):
                        self.submission_batch.add(
                            self.classroom.courses().courseWork().studentSubmissions().list(
                                courseId=cw['courseId'],
                                courseWorkId=cw['id'],
                                fields=','.join(SUBMISSION_FIELDS)
                            )
                        )
                        self.test_list.append(RUBRIC.rubric(RUBRIC_REGEX_KEYS, cw['alternateLink']))

    def handle_submissions(self, request_id, response, exception):
        """Callback for when we've received a list of coursework submissions."""
        if exception is not None:
            print(exception)
            #GCLOGGER.info(exception)
        else:
            #GCLOGGER.info(response)
            #print(response)

            # Store all responses in `test_list`
            if not os.path.exists(str(request_id)+".json"):
                self.test_list.append(response)
                #writefile(str(request_id), str(response))

            # Parse and store submissions
            if 'studentSubmissions' in response:
                #print(resp)
                with ThreadPoolExecutor(max_workers=10) as executor:
                    futures = []
                    writefile('debug-uid', str(response['studentSubmissions']))
                    for i, s in enumerate(response['studentSubmissions']):
                        #print(s['courseWorkId'])
                        if(s['state'] == 'RETURNED'):
                            futures.append(executor.submit(
                                lambda:
                                    RUBRIC.submission(
                                        SUBMISSION_REGEX_KEYS,
                                        s['alternateLink'],
                                        s['courseWorkId'],
                                        self.ref_d,
                                        s['userId'],
                                        s['courseId']
                                    )
                                )
                            )
                    for future in as_completed(futures):
                        result = future.result()
                        self.test_list.append(result)
                        self.sub_list.append(result)

    def fetch(self):
        # First, fetch courses
        self.course_batch.add(self.classroom.courses().list(fields='courses/name,courses/id'))
        self.course_batch.execute()

        # Next, fetch coursework, teachers, and students
        self.course_prop_batch.execute()

        # Parse `test_list` which should contain all responses
        ref_r = str(course_utiljs.formatAll(self.test_list))

        #need script to replace only delimiting single quotes
        #check stack overflow?????
        ref_f = ref_r.replace("'", '"')
        ref_f = ref_f.replace('True', '"True"')
        ref_f = ref_f.replace('False', '"False"')
        ref_f = exc.replace(ref_f)
        writefile('ref_f', ref_f)

        # We'll need this info for processing submissions
        self.ref_d = ast.literal_eval(ref_r)#json.loads(ast.literal_eval(ref_r))

        # Last, fetch submissions
        self.submission_batch.execute()

        return self.sub_list

# Seemingly unused functions?
"""
def courselist(resp):
    #get list of courses mapped to ids
    return course_utiljs.getCourseList(resp, "courses")

def courseWorklist(self, resp):
    #get list of courseWork mapped to ids
    return course_utiljs.getCourseList(resp, "courseWork")

def roster(resp):
    #get list of students&teachers mapped to ids
    return course_utiljs.getRoster(resp)

def course_rosters(resp):
    #get list of students&teachers per course
    return course_utiljs.rosterByCourse(resp)
"""

if __name__ == '__main__':
    fetcher = CourseFetcher()
    submissions = fetcher.fetch()
    write_submissions(submissions)

