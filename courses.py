from gAPI import Create_Service
import pandas as pd
import numpy as np
import json
import csv
from pandas.io.json import json_normalize
from googleapiclient.errors import HttpError
from pprint import pprint

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses']

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

class Course:
    def __init__(self, name):
        self.name = name
        self.user_courses = get_user_courses()
        self.courseId = self.get_courseId()
        self.courseWork = self.get_courseWork()
        self.data = get_course(self.courseId)
        self.description = self.get_description()
        self.updateTime = self.get_updateTime()
        self.name = self.get_name()
        self.alternateLink = self.get_alternateLink()
        self.enrollmentCode = self.get_enrollmentCode()
        self.courseGroupEmail = self.get_courseGroupEmail()
        self.section = self.get_section()
        self.teacherGroupEmail = self.get_teacherGroupEmail()
        self.ownerId = self.get_ownerId()
        self.calendarId = self.get_calendarId()
        self.teacherFolder = self.get_teacherFolder()
    
    def __getitem__(self, key):
        return getattr(self, key)
   
    def list_attr(self):
        attr = self.__dict__.keys()
        for a in attr:
            print(a)

    def list_all(self):
        attr = self.__dict__
        pprint(attr)
        
    
    def get_courseId(self):
        for course in self.user_courses:
            if(json.dumps(course).find(self.name)!= -1):
               self.courseId = course['id']
            else:
                continue
        return self.courseId
    
    def get_courseWork(self):
        return get_course_courseWork(self.courseId)

    def get_description(self):
        try:
            return self.data['description']
        except:
            pass

    def get_updateTime(self):
        return self.data['updateTime']

    def get_name(self):
        return self.data['name']

    def get_alternateLink(self):
        return self.data['alternateLink']

    def get_enrollmentCode(self):
        return self.data['enrollmentCode']


    def get_courseGroupEmail(self):
        return self.data['courseGroupEmail']

    def get_section(self):
        return self.data['section']

    def get_teacherGroupEmail(self):
        return self.data['teacherGroupEmail']

    def get_ownerId(self):
        return self.data['ownerId']

    def get_calendarId(self):
        return self.data['calendarId']

    def get_teacherFolder(self):
        return self.data['teacherFolder']

    def courseWorkGen(self):
        courseWorkObjs = []
        for course in self.courseWork['courseWork']:
            courseWorkObjs.append(CourseWork(self.name, course['id']))
        return courseWorkObjs

class CourseWork(Course):
    def __init__(self, name, courseWorkId):
        self.user_courses = get_user_courses()
        self.name = name
        self.courseId = Course.get_courseId(self)
        self.courseWorkId = courseWorkId
        self.courseWorkData = get_courseWork(self.courseId, self.courseWorkId)
        self.courseWork_submissions = get_courseWork_submissions(self.courseId, self.courseWorkId)
        self.updateTime = self.get_updateTime()
        self.assigneeMode = self.get_assigneeMode()
        self.creatorUserId = self.get_creatorUserId()
        self.dueDate = self.get_dueDate()
        self.state = self.get_state()
        self.dueTime = self.get_dueTime()
        self.topicId = self.get_topicId()
        self.description = self.get_description()
        self.studentWorkFolder = self.get_studentWorkFolder()
        self.title = self.get_title()
        self.maxPoints = self.get_maxPoints()
        self.workType = self.get_workType()
        self.alternateLink = self.get_alternateLink()
        self.materials = self.get_materials()
    
    def __getitem__(self, key):
        return getattr(self, key)
   
    def list_attr(self):
        attr = self.__dict__.keys()
        for a in attr:
            print(a)

    def list_all(self):
        attr = self.__dict__
        pprint(attr)
    

    
    def get_updateTime(self):
        return get_courseWork(self.courseId, self.courseWorkId)['updateTime'] 

    def get_assigneeMode(self):
        return get_courseWork(self.courseId, self.courseWorkId)['assigneeMode']
    
    def get_creatorUserId(self):
        return get_courseWork(self.courseId, self.courseWorkId)['creatorUserId']

    def get_dueDate(self):
        try:
            return get_courseWork(self.courseId, self.courseWorkId)['dueDate']
        except:
            pass

    def get_state(self):
        return get_courseWork(self.courseId, self.courseWorkId)['state']

    def get_dueTime(self):
        try:
            return get_courseWork(self.courseId, self.courseWorkId)['dueTime']
        except:
            pass

    def get_topicId(self):
        try:
            return get_courseWork(self.courseId, self.courseWorkId)['topicId']
        except:
            pass
 
    def get_description(self):
        return get_courseWork(self.courseId, self.courseWorkId)['description']

    def get_studentWorkFolder(self):
        try:
            return get_courseWork(self.courseId, self.courseWorkId)['studentWorkFolder']
        except:
            pass

    def get_title(self):
        return get_courseWork(self.courseId, self.courseWorkId)['title']

    def get_maxPoints(self):
        return get_courseWork(self.courseId, self.courseWorkId)['maxPoints']

    def get_workType(self):
        return get_courseWork(self.courseId, self.courseWorkId)['workType']

    def get_alternateLink(self):
        return get_courseWork(self.courseId, self.courseWorkId)['alternateLink']

    def get_materials(self):
        try:
            return get_courseWork(self.courseId, self.courseWorkId)['materials']    
        except:
            pass

    def submissionGen(self):
        submissionObjs = []
        for submission in self.courseWork_submissions['studentSubmissions']:
            submissionObjs.append(Submission(self.name, self.courseWorkId, submission['id']))
        return submissionObjs

class Submission(CourseWork):
    def __init__(self, name, courseWorkId, submissionId):
        self.submissionId = submissionId
        self.name = name
        self.user_courses = get_user_courses()
        self.courseId = Course.get_courseId(self)
        self.courseWorkId = courseWorkId
        self.data = get_studentSubmission(self.courseId, self.courseWorkId, self.submissionId)
        self.courseWork_submissions = get_courseWork_submissions(self.courseId, self.courseWorkId)
        self.draftGrade =self.get_draftGrade()
        self.updateTime = self.get_updateTime()
        self.alternateLink = self.get_alternateLink()
        self.userId = self.get_userId()
        self.creationTime = self.get_creationTime()
        self.state = self.get_state()
        self.courseWorkType = self.get_courseWorkType()
        self.assignedGrade = self.get_assignedGrade()
    
    def __getitem__(self, key):
        return getattr(self, key)
   
    def list_attr(self):
        attr = self.__dict__.keys()
        for a in attr:
            print(a)

    def list_all(self):
        attr = self.__dict__
        pprint(attr)
    


    def get_draftGrade(self):
        return self.data['draftGrade']
       
    def get_updatetime(self):
        return self.data['updateTime']

    def get_alternateLink(self):
        return self.data['alternateLink']

    def get_userId(self):
        return self.data['userId']

    def get_creationTime(self):
        return self.data['creationTime']

    def get_state(self):
        return self.data['state']  
 
    def get_courseWorkType(self):
        return self.data['courseWorkType']
 
    def get_assignedGrade(self):
        return self.data['assignedGrade']


def get_user_courses():
    return service.courses().list().execute()['courses']

def get_course_courseWork(courseId):
    return service.courses().courseWork().list(courseId=courseId).execute()

def get_course(id):
    return service.courses().get(id=id).execute()


def get_courseWork(courseId, id):
    return service.courses().courseWork().get(courseId=courseId, id=id).execute()

def get_studentSubmission(courseId, courseWorkId, id):
    return service.courses().courseWork().studentSubmissions().get(courseId=courseId, courseWorkId=courseWorkId, id=id).execute()

def get_courseWork_submissions(courseId, courseWorkId):
    return service.courses().courseWork().studentSubmissions().list(courseId=courseId, courseWorkId=courseWorkId).execute()


def getCourse(courseName):
    c = Course(courseName)
    cw = c.courseWorkGen()
    s = []
    for w in cw:
        s.append(w.submissionGen())
    return {'Course': c, 'CourseWork':cw, 'Submissions':s}
