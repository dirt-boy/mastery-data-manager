from gAPI import Create_Service
import json
from pandas.io.json import json_normalize
from googleapiclient.errors import HttpError
from googleapiclient.http import BatchHttpRequest
import page_util as pg
import json
import sys
sys.path.insert(1, 'logging-test')
import makelogger as logger
import httplib2
import extract_data as RUBRIC

GCLOGGER = logger.get_logger(__name__)
REGEX_KEYS = RUBRIC.regex_gen()


CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses']

classroom = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)


def callback_c(request_id, response, exception):
    if exception is not None:
        GCLOGGER.info(exception)
        pass
    else:
        GCLOGGER.info(response)
        itercourses(response)
        pass

def callback_cw(request_id, response, exception):
    if exception is not None:
        GCLOGGER.info(exception)
        pass
    else:
        GCLOGGER.info(response)
        itercourseworks(response)
        pass

def callback_s(request_id, response, exception):
    if exception is not None:
        GCLOGGER.info(exception)
        pass
    else:
        GCLOGGER.info(response)
        pass





batch_c = classroom.new_batch_http_request(callback=callback_c)
batch_cw = classroom.new_batch_http_request(callback=callback_cw)
batch_s = classroom.new_batch_http_request(callback=callback_s)

def user_courses():
    batch_c.add(classroom.courses().list(fields='courses/name,courses/id')) 


def course_coursework(courseId):
    batch_cw.add(classroom.courses().courseWork().list(courseId=courseId, fields='courseWork/id,courseWork/title,courseWork/maxPoints,courseWork/description,courseWork/creationTime,courseWork/alternateLink,courseWork/courseId'))
    

def coursework_submissions(courseId, courseworkId):
    batch_s.add(classroom.courses().courseWork().studentSubmissions().list(courseId=courseId, courseWorkId=courseworkId, fields='studentSubmissions/id,studentSubmissions/assignedGrade,studentSubmissions/alternateLink,studentSubmissions/courseWorkId,studentSubmissions/courseId,studentSubmissions/userId'))


def itercourses(resp):
    for i, c in enumerate(resp['courses']):
        course_coursework(c['id'])

def itercourseworks(resp):
    for i, cw in enumerate(resp['courseWork']):
        coursework_submissions(cw['courseId'], cw['id'])
        RUBRIC.rubric(REGEX_KEYS, cw['alternateLink'])        





user_courses()

batch_c.execute()
batch_cw.execute()
batch_s.execute()









