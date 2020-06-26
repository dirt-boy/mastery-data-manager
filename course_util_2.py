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
    courses = classroom.courses().list().execute()
    userId =  courses['courses'][0]['ownerId']
    courseIds = []

    for c in courses['courses']:
        courseIds.append(c['id'])
    print([userId, courseIds])
    return [userId, courseIds]

def course_coursework(courseId):
    coursework = classroom.courses().courseWork().list(courseId=courseId).execute()
    courseworkIds = []
    for c in coursework['courseWork']:
        courseworkIds.append(c['id'])
    return courseworkIds

def coursework_submissions(courseId, courseworkId):    
    submissions = classroom.courses().courseWork().studentSubmissions().list(courseId=courseId, courseWorkId=courseworkId).execute()
    submissionIds = []
    for s in submissions['studentSubmissions']:
        submissionIds.append(s['id'])
    return submissionIds

def student_roster(courseId):
    students = classroom.list(courseId)
    return students

def teacher_roster(courseId):
    teachers = classroom.list(courseId)
    return teachers

def course_dict():
    course_dict = {}
    courses = user_courses()
    userId = courses[0]
    course_dict['userId'] = userId
    course_dict['userCourses'] = []
    course_ids = courses[1]

    for i,cid in enumerate(course_ids):
        coursework = course_coursework(cid)
        course_name = classroom.courses().get(id=cid).execute()['name']
        course_dict['userCourses'].append({'name':course_name, 'id':cid, 'coursework': []})
        for j,cwid in enumerate(coursework):
            coursework_name = classroom.courses().courseWork().get(courseId=cid, id=cwid).execute()['title']
            course_dict['userCourses'][i]['coursework'].append({'title': coursework_name, 'courseWorkId': cwid, 'content':[] })
            submissions = coursework_submissions(courseId=cid, courseworkId=cwid)
            for k,sid in enumerate(submissions):
                studentId = classroom.courses().courseWork().studentSubmissions().get(courseId=cid, courseWorkId=cwid, id=sid).execute()['userId']
                try:
                    grade = classroom.courses().courseWork().studentSubmissions().get(courseId=cid, courseWorkId=cwid, id=sid).execute()['assignedGrade']
                except:
                    print('No assigned grade available for course "'+coursework_name+', submission '+ str(studentId)+'. Continuing construction...')
                    if(k%2==0):
                        "Working...."
                    else:
                        "still.... working... dont worry..."
                    grade = 'Ungraded'
                finally:

                    alternateLink = classroom.courses().courseWork().studentSubmissions().get(courseId=cid, courseWorkId=cwid, id=sid).execute()['alternateLink']
                    course_dict['userCourses'][i]['coursework'][j]['content'].append({'studentId':studentId, 'assignedGrade':grade, 'alternateLink':alternateLink})


    return course_dict



def write_file(course_dict):
    name = str(user_courses()[0])+'.json' 
    with open(name, 'x') as coursefile:
        coursefile.write(course_dict)
    print("New Course File written: "+name+".\nPlease check current directory for results.")
    return coursefile
    
write_file(course_dict())
    





