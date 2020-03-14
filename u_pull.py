from gAPI import Create_Service
import course_util as cutil


u_courses = cutil.get_user_courses()

t_courses = []
for course in u_courses:
       t_courses.append(cutil.getCourse(course["name"]))


for i in range(len(t_courses)):
    print t_courses[i]['Course'].name








