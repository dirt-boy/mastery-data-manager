import json
import os
from gAPI import Create_Service
from course_util import (CourseFetcher, write_submissions)
from concurrent.futures import (
    as_completed,
    ThreadPoolExecutor
)

TOKEN_DIR = "data/tokens"
CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses https://www.googleapis.com/auth/classroom.rosters https://www.googleapis.com/auth/classroom.profile.emails https://www.googleapis.com/auth/classroom.rosters']

def get_classroom_data(token):
    print("\n-------------- Fetching classroom data with %s ----------------" % token)

    # Fetch all submissions that are accessible with the specified token
    classroom = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES, token_path=os.path.join(TOKEN_DIR, token))
    fetcher = CourseFetcher(classroom=classroom)
    submissions = fetcher.fetch()

    # Write the submissions to a token-suffixed file for validation
    write_submissions(submissions, filename_suffix=os.path.splitext(os.path.basename(token))[0])
    return submissions

if __name__ == '__main__':
    course_info = {}
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for token in os.listdir(TOKEN_DIR):
            print(os.path.join(TOKEN_DIR, token))
            future = executor.submit(lambda: get_classroom_data(token))
            futures.append(future)
            break

        # Aggregate all of the submissions from the different tokens
        all_submissions = []
        for future in as_completed(futures):
            submissions = future.result()

            # TODO: do we need to de-dup?
            all_submissions += submissions
