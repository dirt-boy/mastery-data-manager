"""Main logic file. Manages data pipeline."""
import json
import os
import sys

from gAPI import Create_Service

sys.path.insert(1, 'logging-test')
import extract_data as RUBRIC
import js2py
import makelogger as logger

js2py.translate_file('course_util.js', 'course_utiljs.py')
import find_except as exc
import to_csv as csv
from course_utiljs import course_utiljs

GCLOGGER = logger.get_logger(__name__)
RUBRIC_REGEX_KEYS = RUBRIC.regex_gen(0)
SUBMISSION_REGEX_KEYS = RUBRIC.regex_gen(1)


CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses https://www.googleapis.com/auth/classroom.rosters https://www.googleapis.com/auth/classroom.profile.emails https://www.googleapis.com/auth/classroom.rosters']

classroom = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

#testing write to file before logging. commenting out logs

test_list = []
sub_list = []

def callback_c(request_id, response, exception):
    if exception is not None:
        #GCLOGGER.info(exception)
        print(exception)
        pass
    else:
        #GCLOGGER.info(response)
        if(os.path.exists(str(request_id)+".json")):
            pass
        else:
            #writefile(str(request_id), str(response))
            test_list.append(response)
        itercourses(response)
        iterteachers(response)
        iterstudents(response)
        pass

def callback_cw(request_id, response, exception):
    if exception is not None:
        #GCLOGGER.info(exception)
        print(exception)
        pass
    else:
        #GCLOGGER.info(response)
        #print(response)
        if(os.path.exists(str(request_id)+".json")):
            pass
        else:
            #writefile(str(request_id), str(response))
            test_list.append(response)
        itercourseworks(response)
        pass

def callback_s(request_id, response, exception):
    if exception is not None:
        print(exception)
        #GCLOGGER.info(exception)
        pass
    else:
        #GCLOGGER.info(response)
        #print(response)
        if(os.path.exists(str(request_id)+".json")):
            pass
        else:
            test_list.append(response)
            #writefile(str(request_id), str(response))
        itersubmissions(response)
        pass

batch_c = classroom.new_batch_http_request(callback=callback_c)
batch_cw = classroom.new_batch_http_request(callback=callback_cw)
batch_s = classroom.new_batch_http_request(callback=callback_s)

def user_courses():
    #print('USER COURSES:\n')
    batch_c.add(classroom.courses().list(fields='courses/name,courses/id'))


def course_teachers(courseId):
    #print('COURSE TEACHERS:\n')
    batch_cw.add(classroom.courses().teachers().list(courseId=courseId, fields='teachers/courseId,teachers/userId,teachers/profile'))


def course_students(courseId):
    #print('COURSE STUDENTS:\n')
    batch_cw.add(classroom.courses().students().list(courseId=courseId, fields='students/courseId,students/userId,students/profile'))


def course_coursework(courseId):
    #print('COURSE COURSEWORK\n')
    batch_cw.add(classroom.courses().courseWork().list(courseId=courseId, fields='courseWork/id,courseWork/title,courseWork/maxPoints,courseWork/description,courseWork/creationTime,courseWork/alternateLink,courseWork/courseId'))


def coursework_submissions(courseId, courseworkId):
    #print('COURSEWORK SUBMISSIONS\n')
    batch_s.add(classroom.courses().courseWork().studentSubmissions().list(courseId=courseId, courseWorkId=courseworkId, fields='studentSubmissions/id,studentSubmissions/assignedGrade,studentSubmissions/alternateLink,studentSubmissions/courseWorkId,studentSubmissions/courseId,studentSubmissions/userId,studentSubmissions/state'))


def iterteachers(resp):
    #print('TEACHERS:\n')
    for i, t in enumerate(resp['courses']):
        course_teachers(t['id'])

def iterstudents(resp):
    #print('STUDENTS:\n')
    for i, st in enumerate(resp['courses']):
        course_students(st['id'])

def itercourses(resp):
    #print('COURSES:\n')
    for i, c in enumerate(resp['courses']):
        course_coursework(c['id'])

def itercourseworks(resp):
    #print('COURSEWORKS:\n')
    #print(resp)
    if 'courseWork' in resp:
        for i, cw in enumerate(resp['courseWork']):
            if ('Project' in cw['title'] and 'Ticket' not in cw['title'] and 'Do Now' not in cw['title'] and 'Slides' not in cw['title'] and 'Day' not in cw['title']):
                coursework_submissions(cw['courseId'], cw['id'])
                test_list.append(

                    RUBRIC.rubric(RUBRIC_REGEX_KEYS, cw['alternateLink'])

                    )

def itersubmissions(resp):
    #print('SUBMISSIONS:\n')
    if 'studentSubmissions' in resp:
        print(resp)
        writefile('debug-uid', str(resp['studentSubmissions']))
        for i, s in enumerate(resp['studentSubmissions']):
            #print(s['courseWorkId'])
            if(s['state'] == 'RETURNED'):
                test_list.append(RUBRIC.submission(SUBMISSION_REGEX_KEYS, s['alternateLink'], s['courseWorkId'], ref_d, s['userId'], s['courseId']))
                sub_list.append(RUBRIC.submission(SUBMISSION_REGEX_KEYS, s['alternateLink'], s['courseWorkId'], ref_d, s['userId'], s['courseId']))
            else:
                pass


def writefile(name, content):
    save_path = os.path.abspath("logs")
    completename = os.path.join(save_path, str(name))
    with open(completename+".json", "w") as f:
        f.write(content)

def log_all(results):
    for res, l in enumerate(results):
        GCLOGGER.info(res)

def format_all(results):
    return course_utiljs.formatAll(results)

def courselist(resp):
    #get list of courses mapped to ids
    return course_utiljs.getCourseList(resp, "courses")

def courseWorklist(resp):
    #get list of courseWork mapped to ids
    return course_utiljs.getCourseList(resp, "courseWork")

def roster(resp):
    #get list of students&teachers mapped to ids
    return course_utiljs.getRoster(resp)

def course_rosters(resp):
    #get list of students&teachers per course
    return course_utiljs.rosterByCourse(resp)

def pullbase():
    user_courses()
    batch_c.execute()
    batch_cw.execute()
    #batch_s.execute()
    return str(course_utiljs.formatAll(test_list))
    #return(str(test_list))

ref_r = pullbase()

#need script to replace only delimiting single quotes
#check stack overflow?????


ref_f = ref_r.replace("'", '"')
ref_f = ref_f.replace('True', '"True"')
ref_f = ref_f.replace('False', '"False"')


ref_f = exc.replace(ref_f)


writefile('ref_f', ref_f)
ref_d = json.loads(ref_f)


def pullcustom():
    batch_s.execute()
    return sub_list


string = json.dumps(pullcustom(), sort_keys=True, indent=4)
writefile('submissions', string)
csv.fullconvert()
