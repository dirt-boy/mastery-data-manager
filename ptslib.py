import requests
//import login-lib.py

def get_url():
    //depends on rubric.list vs courseworkquery    
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
    

