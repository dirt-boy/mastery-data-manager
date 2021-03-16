"""Sets up a service to connect with Google sheets."""
import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def create_service(client_secret, api_service, api_version, scopes):
    cred = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:

        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open('token.pickle', 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print('Service created succesfully')
        return service
    except Exception as e:
        print(e)
        return None

def doThing():

    service = create_service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
    spreadsheet = {
        'properties': {
            'title': 'title'
        }
    }

    spreadsheet = service.spreadsheets().create(body=spreadsheet,fields='spreadsheetId').execute()
    print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))

doThing()
