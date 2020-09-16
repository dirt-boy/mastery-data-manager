__all__ = ['course_utiljs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['getRoster', 'formatAll', 'getCourseList', 'rosterByCourse'])
@Js
def PyJsHoisted_getCourseList_(courseData, prop, this, arguments, var=var):
    var = Scope({'courseData':courseData, 'prop':prop, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'courseData', 'i', 'titles', 'prop'])
    var.put('titles', Js({}))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<=var.get('courseData').get('length')):
        try:
            if (PyJsStrictEq(var.get('courseData').get(var.get('i')).typeof(),Js('object')) and var.get('courseData').get(var.get('i')).get(var.get('prop'))):
                #for JS loop
                var.put('j', Js(0.0))
                while (var.get('j')<=var.get('courseData').get(var.get('i')).get(var.get('prop')).get('length')):
                    try:
                        if var.get('courseData').get(var.get('i')).get(var.get('prop')).get(var.get('j')):
                            var.get('titles').put(var.get('courseData').get(var.get('i')).get(var.get('prop')).get(var.get('j')).get('id'), (var.get('courseData').get(var.get('i')).get(var.get('prop')).get(var.get('j')).get('title') or var.get('courseData').get(var.get('i')).get(var.get('prop')).get(var.get('j')).get('name')))
                    finally:
                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('titles')
PyJsHoisted_getCourseList_.func_name = 'getCourseList'
var.put('getCourseList', PyJsHoisted_getCourseList_)
@Js
def PyJsHoisted_getRoster_(resp, this, arguments, var=var):
    var = Scope({'resp':resp, 'this':this, 'arguments':arguments}, var)
    var.registers(['roster', 'i', 'resp', 'j'])
    var.put('roster', Js({'teachers':Js({}),'students':Js({})}))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<=var.get('resp').get('length')):
        try:
            if (PyJsStrictEq(var.get('resp').get(var.get('i')).typeof(),Js('object')) and (var.get('resp').get(var.get('i')).get('teachers') or var.get('resp').get(var.get('i')).get('students'))):
                if var.get('resp').get(var.get('i')).get('teachers'):
                    #for JS loop
                    var.put('j', Js(0.0))
                    while (var.get('j')<=var.get('resp').get(var.get('i')).get('teachers').get('length')):
                        try:
                            if var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')):
                                var.get('roster').get('teachers').put(var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('userId'), var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('profile').get('name').get('fullName'))
                        finally:
                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                if var.get('resp').get(var.get('i')).get('students'):
                    #for JS loop
                    var.put('j', Js(0.0))
                    while (var.get('j')<=var.get('resp').get(var.get('i')).get('students').get('length')):
                        try:
                            if var.get('resp').get(var.get('i')).get('students').get(var.get('j')):
                                var.get('roster').get('students').put(var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('userId'), var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('profile').get('name').get('fullName'))
                        finally:
                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('roster')
PyJsHoisted_getRoster_.func_name = 'getRoster'
var.put('getRoster', PyJsHoisted_getRoster_)
@Js
def PyJsHoisted_rosterByCourse_(resp, this, arguments, var=var):
    var = Scope({'resp':resp, 'this':this, 'arguments':arguments}, var)
    var.registers(['roster', 'i', 'resp', 'j'])
    var.put('roster', Js({}))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<=var.get('resp').get('length')):
        try:
            if (PyJsStrictEq(var.get('resp').get(var.get('i')).typeof(),Js('object')) and (var.get('resp').get(var.get('i')).get('teachers') or var.get('resp').get(var.get('i')).get('students'))):
                if var.get('resp').get(var.get('i')).get('teachers'):
                    #for JS loop
                    var.put('j', Js(0.0))
                    while (var.get('j')<=var.get('resp').get(var.get('i')).get('teachers').get('length')):
                        try:
                            if ((var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')) and var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('courseId')) and var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('userId')):
                                if var.get('roster').get(var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('courseId')):
                                    var.get('roster').get(var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('courseId')).get('teachers').put(var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('userId'), var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')))
                                if var.get('roster').get(var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('courseId')).neg():
                                    var.get('roster').put(var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('courseId'), Js({'teachers':Js({}),'students':Js({})}))
                                    var.get('roster').get(var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('courseId')).get('teachers').put(var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')).get('userId'), var.get('resp').get(var.get('i')).get('teachers').get(var.get('j')))
                        finally:
                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                if var.get('resp').get(var.get('i')).get('students'):
                    #for JS loop
                    var.put('j', Js(0.0))
                    while (var.get('j')<=var.get('resp').get(var.get('i')).get('students').get('length')):
                        try:
                            if ((var.get('resp').get(var.get('i')).get('students').get(var.get('j')) and var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('courseId')) and var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('userId')):
                                if var.get('roster').get(var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('courseId')):
                                    var.get('roster').get(var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('courseId')).get('students').put(var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('userId'), var.get('resp').get(var.get('i')).get('students').get(var.get('j')))
                                if var.get('roster').get(var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('courseId')).neg():
                                    var.get('roster').put(var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('courseId'), Js({'teachers':Js({}),'students':Js({})}))
                                    var.get('roster').get(var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('courseId')).get('students').put(var.get('resp').get(var.get('i')).get('students').get(var.get('j')).get('userId'), var.get('resp').get(var.get('i')).get('students').get(var.get('j')))
                        finally:
                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('roster')
PyJsHoisted_rosterByCourse_.func_name = 'rosterByCourse'
var.put('rosterByCourse', PyJsHoisted_rosterByCourse_)
@Js
def PyJsHoisted_formatAll_(response, this, arguments, var=var):
    var = Scope({'response':response, 'this':this, 'arguments':arguments}, var)
    var.registers(['response'])
    return Js({'courses':var.get('getCourseList')(var.get('response'), Js('courses')),'courseWork':var.get('getCourseList')(var.get('response'), Js('courseWork')),'roster':var.get('getRoster')(var.get('response')),'rosterByCourse':var.get('rosterByCourse')(var.get('response'))})
PyJsHoisted_formatAll_.func_name = 'formatAll'
var.put('formatAll', PyJsHoisted_formatAll_)
pass
pass
pass
pass
pass


# Add lib to the module scope
course_utiljs = var.to_python()