#!/usr/bin/env python
import pandas as pd
import ast
import course_util as c
import json

course = c.pullall()
course_d = course.replace("'", '"')
course_d = course_d.replace('True', '"True"')
course_d = json.loads(course_d)

def convert(data):

    df = pd.read_json(data)
    df.to_csv()

    return df

def getvals(course_d, level=None):
    course_d = course_d
    if level==None:
        return list(data.values())
    else:
        return list(data[level].values())

def getkeys(course_d, level=None):
    course_d = course_d
    if level==None:
        return list(data.keys())
    else:
        return list(data[level].keys())

def getkey_by_val(course_d, key, name=None):
    course_d = course_d
    res = []
    if name==None:

        for i, k in enumerate(key):
            #print(data[key])
            res.append(data[k])
    else:
        
        #try lookup by val
        for i, k in enumerate(key):
            
            val = list(data[k].keys())[list(data[k].values()).index(name)]
            print(val)
            res.append(data[k][str(val)])
    return res

print(course_d)
        


        


