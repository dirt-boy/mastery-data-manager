from gAPI import Create_Service
import json
from pandas.io.json import json_normalize
from googleapiclient.errors import HttpError
from googleapiclient.http import BatchHttpRequest
import page_util as pg
import json
import os.path
from os import path
import sys
sys.path.insert(1, 'logging-test')
import makelogger as logger
import httplib2
import extract_data as RUBRIC
import js2py
js2py.translate_file('course_util.js', 'course_utiljs.py')
from course_utiljs import course_utiljs

GCLOGGER = logger.get_logger(__name__)
REGEX_KEYS = RUBRIC.regex_gen()


CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses https://www.googleapis.com/auth/classroom.rosters https://www.googleapis.com/auth/classroom.profile.emails']

classroom = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

#testing write to file before logging. commenting out logs

test_list = []

def callback_c(request_id, response, exception):
    if exception is not None:
        #GCLOGGER.info(exception)
        print(exception)
        pass
    else:
        #GCLOGGER.info(response)
        if(path.exists(str(request_id)+".json")):
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
        if(path.exists(str(request_id)+".json")):
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
        if(path.exists(str(request_id)+".json")):
            pass
        else:
            test_list.append(response)
            #writefile(str(request_id), str(response))
        pass

batch_c = classroom.new_batch_http_request(callback=callback_c)
batch_cw = classroom.new_batch_http_request(callback=callback_cw)
batch_s = classroom.new_batch_http_request(callback=callback_s)

def user_courses():
    batch_c.add(classroom.courses().list(fields='courses/name,courses/id'))


def course_teachers(courseId):
    batch_cw.add(classroom.courses().teachers().list(courseId=courseId, fields='teachers/courseId,teachers/userId,teachers/profile'))


def course_students(courseId):
    batch_cw.add(classroom.courses().students().list(courseId=courseId, fields='students/courseId,students/userId,students/profile'))


def course_coursework(courseId):
    batch_cw.add(classroom.courses().courseWork().list(courseId=courseId, fields='courseWork/id,courseWork/title,courseWork/maxPoints,courseWork/description,courseWork/creationTime,courseWork/alternateLink,courseWork/courseId'))


def coursework_submissions(courseId, courseworkId):
    batch_s.add(classroom.courses().courseWork().studentSubmissions().list(courseId=courseId, courseWorkId=courseworkId, fields='studentSubmissions/id,studentSubmissions/assignedGrade,studentSubmissions/alternateLink,studentSubmissions/courseWorkId,studentSubmissions/courseId,studentSubmissions/userId'))


def iterteachers(resp):
    for i, t in enumerate(resp['courses']):
        course_teachers(t['id'])

def iterstudents(resp):
    for i, st in enumerate(resp['courses']):
        course_students(st['id'])

def itercourses(resp):
    for i, c in enumerate(resp['courses']):
        course_coursework(c['id'])

def itercourseworks(resp):
    if hasattr(resp, 'courseWork'):
        for i, cw in enumerate(resp['courseWork']):
            coursework_submissions(cw['courseId'], cw['id'])
            test_list.append(RUBRIC.rubric(REGEX_KEYS, cw['alternateLink']))

def writefile(name, content):
    save_path = "/Users/gg/NerdStuff/mastery-data-manager/logs"
    completename = os.path.join(save_path, str(name))
    with open(completename+".json", "w") as f:
        f.write(content)

def log_all(results):
    for res, l in enumerate(results):
        GCLOGGER.info(res)

def format_all(results):
    return courseutiljs.formatAll(resp)

def courselist(resp):
    #get list of courses mapped to ids
    return course_utiljs.getCourseList(resp, "courses")

def courseWorklist(resp):
    #get list of courseWork mapped to ids
    return course_utiljs.getCourseList(resp, "courseWork")

def roster(resp):
    #get list of students&teachers mapped to ids
    return course_utiljs.getRoster(resp)



user_courses()

batch_c.execute()
batch_cw.execute()
batch_s.execute()
print(str(test_list))
# log_all(test_list)
