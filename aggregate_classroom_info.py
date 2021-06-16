import json
import os
from gAPI import Create_Service_Direct
from course_util import (CourseFetcher, write_submissions, writefile)
from concurrent.futures import (
    as_completed,
    ThreadPoolExecutor
)
import to_csv
from copy import copy
import pickle
import uuid


TOKEN_DIR = "data/tokens"
CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses https://www.googleapis.com/auth/classroom.rosters https://www.googleapis.com/auth/classroom.profile.emails https://www.googleapis.com/auth/classroom.rosters']
SERVICE_ACCOUNT_PATH = "/Users/gg/NerdStuff/mastery-data-manager/data/etc/gspread_service_account.json"


def get_classroom_data(token):
    print("\n-------------- Fetching classroom data with %s ----------------" % token)
    # Fetch all submissions that are accessible with the specified token
    classroom = Create_Service_Direct(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES, token=token)
    fetcher = CourseFetcher(classroom=classroom)
    submissions = fetcher.fetch()

# Write the submissions to a token-suffixed file for validation
    suffix = str(uuid.uuid4())
    write_submissions(submissions, filename_suffix=suffix[:8])
    return submissions

def run():
    tokens = unpickler()
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for token in tokens:
            print("using following token: ", str(token))
            future = executor.submit(lambda: get_classroom_data(token))
            futures.append(future)  
            # Aggregate all of the submissions from the different tokens
        all_submissions = []
        for future in as_completed(futures):
            submissions = future.result()

            # TODO: do we need to de-dup?
            all_submissions += submissions

    to_csv.fullconvert()


def unpickle(token):
    return pickle.loads(open("data/tokens/"+str(token), "rb").read())

def unpickler():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for token in os.listdir(TOKEN_DIR):
            future = executor.submit(lambda: unpickle(token))
            futures.append(future)
        all_tokens = []
        for future in as_completed(futures):
            t = future.result()
            all_tokens.append(t)
    return all_tokens
                
       


if __name__ == '__main__':
    run()

