from gAPI import Create_Service
import json
from pandas.io.json import json_normalize
from googleapiclient.errors import HttpError
from googleapiclient.http import BatchHttpRequest
import page_util as pg
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel('INFO')



CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses']

classroom = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)


def callback(request_id, response, exception):
    if exception is not None:
        print('Error accessing object data for request: '+ str(request_id))
        
    else:
        print('Data accessed succesfully.')
        logger.info(response)
        return response

batch_cw = classroom.new_batch_http_request(callback=callback)
batch_s = classroom.new_batch_http_request(callback=callback)

def user_courses():

    courses = classroom.courses().list(fields='courses/name,courses/id').execute() 
    return courses


def course_coursework(courseId):
    return batch_cw.add(classroom.courses().courseWork().list(courseId=courseId, fields='courseWork/id,courseWork/title,courseWork/maxPoints,courseWork/description,courseWork/creationTime,courseWork/alternateLink'), request_id=courseId)
    

def coursework_submissions(courseId, courseworkId, i):
    req_id = str(courseworkId)+str(i)
    return batch_s.add(classroom.courses().courseWork().studentSubmissions().list(courseId=courseId, courseWorkId=courseworkId, fields='studentSubmissions/id, studentSubmissions/assignmentSubmission/userId,studentSubmissions/assignedGrade,studentSubmissions/alternateLink'),request_id=req_id)


def student_roster(courseId):
    students = classroom.list(courseId)
    return students

def teacher_roster(courseId):
    teachers = classroom.list(courseId)
    return teachers

def course_dict():
    course_dict = user_courses()
    print('pre batch-execute')
    batch_cw.execute()
    print('post batch-execute')

    coursework = get_coursework(course_dict)
    
    for i,c in enumerate(coursework['courses']):

        print('entered first loop...')

        course_dict['courses'][i]['courseWork'] = []
        course_dict['courses'][i]['courseWork'].append(c['courseWork'])
        
        print('pre get_submissions...')
        
        get_submissions(course_dict, i, c['id'])

        print('post get_submissions...')
        submissions = batch_s.execute()
        print('post batch execute...')
        for j,cw in enumerate(course_dict['courses'][i]['courseWork']):
            

            course_dict['courses'][i]['courseWork'][j]['studentSubmissions'] = []
            
            course_dict['courses'][i]['courseWork'][j]['studentSubmissions'].append(cw)
    return course_dict
            

def get_coursework(course_dict):
    for i,c in enumerate(course_dict['courses']):
        course_dict['courses'][i] = course_coursework(c['id'])
        return course_dict

def get_submissions(course_dict, i, cwid):
    for i,cw in enumerate(course_dict['courses']):
        return coursework_submissions(cw['id'], cwid, i)


def execute_batch():

    response = batch.execute(http=http)
    print(response)

def write_file(course_dict):
    name = str('courses')+'.json'
    with open(name, 'w') as coursefile:
        coursefile.write(str(course_dict))
    return coursefile


write_file(course_dict())





