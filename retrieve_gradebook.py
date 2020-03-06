from gAPI import Create_Service
import pandas as pd
import numpy as np
import json
import csv
from pandas.io.json import json_normalize
from googleapiclient.errors import HttpError


CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses']

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

class Course:
    def __init__(self,class_name):
        self.class_name = class_name
        self.id = self.get_class_id()

    def get_class_id(self):
        my_courses = get_courses()
        for course in my_courses:
            if(json.dumps(course[0]).find(self.class_name)!= -1):
                self.id = json.dumps(course[1]).strip('"')
        return self.id
        
    def get_coursework(self):
        courseworks = []
        aslist = [self.id]
        self.coursework = get_coursework(aslist)
        for course in self.coursework[0]['courseWork']:
            courseworks.append(CourseWork(self.class_name, course['id']))
        self.coursework = courseworks
        return self.coursework

    #this needs to be edited to return a dict or list of submissions tied to each course
    def get_submissions(self, coursework):
        #coursework_id = [coursework[0]['courseWork'][0]['id']]
        l_submissions = []
        coursework_ids = isolate_cw_ids(coursework)
        for id in coursework_ids:
            l_submissions.append(service.courses().courseWork().studentSubmissions().list(courseId=self.id, courseWorkId=id).execute())
        self.submissions = l_submissions
        return self.submissions

class CourseWork(Course):
    def __init__(self, class_name, courseWorkId):
        Course.__init__(self, class_name)
        self.courseId = Course.get_class_id(self)
        self.courseWorkId = courseWorkId
        self.l_submissions = []
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

    def make_submissions(self):
        l_submissions = []
        for submission in self.submissions[0]['studentSubmissions']:
            l_submissions.append(Submission(self.class_name, submission['id']))
        self.l_submissions = l_submissions

    def describe(self):
        print("Class Name: ", self.class_name)
        print("Course Work: ", self.coursework)
        print("Submissions: ", self.l_submissions)
      
         

        


class Submission(CourseWork):
    def __init__(self, class_name, s_id):
        CourseWork.__init__(self, class_name)
        self.draftGrade =self.get_draftGrade()
        self.updateTime = self.get_updateTime()
        self.alternateLink = self.get_alternateLink()
        self.userId = self.get_userId()
        self.creationTime = self.get_creationTime()
        self.state = self.get_state()
        self.courseWorkType = self.get_courseWorkType()
        self.assignedGrade = self.get_assignedGrade()
        self.maxPoints = self.get_maxPoints()    
        self.s_id = s_id        

    def get_draftGrade(self):
        return get_studentSubmission(self.classId, self.courseWorkId, self.id)[0]['studentSubmissions'][0]['draftGrade']
       
    def get_updateTime(self):
        return get_studentSubmission(self.classId, self.courseWorkId, self.id)[0]['studentSubmissions'][0]['updateTime']

    def get_alternateLink(self):
        return get_studentSubmission(self.classId, self.courseWorkId, self.id)[0]['studentSubmissions'][0]['alternateLink']

    def get_userId(self):
        return get_studentSubmission(self.classId, self.courseWorkId, self.id)[0]['studentSubmissions'][0]['userId']

    def get_creationTime(self):
        return get_studentSubmission(self.classId, self.courseWorkId, self.id)[0]['studentSubmissions'][0]['creationTime']

    def get_state(self):
        return get_studentSubmission(self.classId, self.courseWorkId, self.id)[0]['studentSubmissions'][0]['state']
   
    def get_courseWorkId(self):
        return get_studentSubmission(self.classId, self.courseWorkId, self.id)[0]['studentSubmissions'][0]['courseWorkId']
   
    def get_courseWorkType(self):
        return get_studentSubmission(self.classId, self.courseWorkId, self.id)[0]['studentSubmissions'][0]['courseWorkType']
  
    def get_assignedGrade(self):
        return get_studentSubmission(self.classId, self.courseWorkId, self.id)[0]['studentSubmissions'][0]['assignedGrade']

    def get_maxPoints(self):
        return get_studentSubmission(self.classId, self.courseWorkId, self.id)[0]['studentSubmissions'][0]['submissionHistory'][2]['gradeHistory']['maxPoints']
    
    

def get_courses():
    raw_response_data = service.courses().list().execute()
    response_data = raw_response_data['courses']
    l_response = []
    for course in response_data:
        l_response.append((course['name'], course['id']))
    return l_response

def get_course(id):
    return service.courses().get(id=id).execute()

def get_courseWork(courseId, id):
    return service.courses().courseWork().get(courseId=courseId, id=id).execute()

def get_studentSubmission(courseId, courseWorkId, id):
    return service.courses().courseWork().studentSubmissions().get(courseId=courseId, courseWorkId=courseWorkId, id=id)


def isolate_ids(courses):
    ids = []
    for course in courses:
        ids.append(course[1])
    return ids

def get_coursework(course_ids):
    raw_response_data = []
    for i in range(len(course_ids)):
        id = course_ids[i]
        raw_response_data.append(service.courses().courseWork().list(courseId=id).execute())
    return json.loads(json.dumps(raw_response_data))

def isolate_cw_ids(coursework):
    ids = []
    for work in coursework[0]['courseWork']:
        ids.append(work['id'])
    return ids

def get_submissions(course_ids, coursework_ids):
    raw_response_data = []
    for i in range(len(course_ids)):
        for j in range(len(coursework_ids)):
            try:
                raw_response_data.append(service.courses().courseWork().studentSubmissions().list(courseId=course_ids[i], courseWorkId=coursework_ids[j]).execute())
                return raw_response_data
            except HttpError as err:
                if err.resp.status in [403, 500, 503]:
                    time.sleep(5)
                else: raise




#the following will spit out a list of all submissions!
#courses = get_courses()
#ids = isolate_ids(courses)
#coursework = get_coursework(ids)
#cw_ids = isolate_cw_ids(coursework)
#raw_submissions = get_submissions(ids, cw_ids)
#submissions = raw_submissions[0]['studentSubmissions']

myCourse = Course('Code Nation Test')

def describe(course):
    courseworks = myCourse.get_coursework()
    for coursework in courseworks:
        print(coursework.class_name)
        print(coursework.title)
        print(coursework.description)
        print(coursework.maxPoints)
        
       
describe(myCourse) 
