from gAPI import Create_Service
import json
from pandas.io.json import json_normalize
from googleapiclient.errors import HttpError
import page_util as pg
import json


CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses']

classroom = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

def user_courses():
    courses = classroom.courses().list(fields='courses/name,courses/id').execute() 
    return courses

def course_coursework(courseId):
    courseWork = classroom.courses().courseWork().list(courseId=courseId, fields='courseWork/id,courseWork/title,courseWork/maxPoints,courseWork/description,courseWork/creationTime,courseWork/alternateLink').execute()
    return courseWork

def coursework_submissions(courseId, courseworkId):    
    submissions = classroom.courses().courseWork().studentSubmissions().list(courseId=courseId, courseWorkId=courseworkId, fields='studentSubmissions/id, studentSubmissions/userId,studentSubmissions/assignedGrade,studentSubmission/alternateLink').execute()
    return submissions


def student_roster(courseId):
    students = classroom.list(courseId)
    return students

def teacher_roster(courseId):
    teachers = classroom.list(courseId)
    return teachers

def course_dict():
    course_dict = user_courses()['courses']

    for i,c in enumerate(course_dict):

        c['courseWork'] = []
        c['courseWork'].append(course_coursework(c['id']))

        for j,cw in enumerate(course_dict[i]['courseWork']):

            cw['studentSubmissions'] = []
            cw['studentSubmissions'].append(coursework_submissions(c['courseWork'][i], cw['courseWork'][j]['id']))

    return course_dict



def write_file(course_dict):
    name = str('courses')+'.json'
    with open(name, 'w') as coursefile:
        coursefile.write(json.dumps(course_dict))
    return coursefile


write_file(course_dict())





