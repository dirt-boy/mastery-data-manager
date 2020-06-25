from gAPI import Create_Service
import json
from pandas.io.json import json_normalize
from googleapiclient.errors import HttpError
import page_util as pg


CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses']

classroom = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

def user_courses():
    courses = classroom.courses().list().execute()
    userId =  courses['courses'][0]['ownerId']
    courseIds = []

    for c in courses['courses']:
        courseIds.append(c['id'])

    return [userId, courseIds]

def course_coursework(courseId):
    coursework = classroom.list(courseId)
    return coursework

def coursework_submissions(courseId, courseworkId):    
    submissions = classroom.list(courseId, courseworkId)
    return submissions

def student_roster(courseId):
    students = classroom.list(courseId)
    return students

def teacher_roster(courseId):
    teachers = classroom.list(courseId)
    return teachers

def course_dict():
    course_dict = {}

    #format: [ int, [int, int] ]
    courses = user_courses()

    #int
    userId = courses[0]

    #list
    course_ids = courses[1]

    for id in course_ids:
        print(id)
        print(classroom.courses().get(id))
        #course_dict[classroom.courses().get(id).execute()['name']] = id

    print(course_dict)
    return course_dict



print(course_dict())
    
    

    





