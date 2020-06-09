import requests
//import login-lib.py

def get_url(type):
    if(type== "list"):
        url= "https://classroom.google.com/u/1/v7/rubric/list?_reqid=1163629&rt=j"
    if(type=="submission"):
        url="https://classroom.google.com/u/1/v7/querysubmission?_reqid=1482657&rt=j"
    return url

def get_headers():
    //pipe from gapis oauth2 lib 
    return headers

def get_payload():
    //pipe from gapis oauth2 lib
    return payload


def by-courseWorkId(courseId, courseWorkId):
    response = requests.request("POST", url, headers=headers, data=payload)
    return response
    

