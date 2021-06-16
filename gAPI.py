"""Google API client"""
from __future__ import print_function

import os
import pickle

import google_login as LOGIN
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def Create_Service(client_secret_file, api_name, api_version, *scopes, token_path='token.pickle'):
    """
    Creates a Google API Client.

    Args:
        client_secret_file (str): path to the credentials.json file
        api_name (str): the name of the API to connect to (ex: "classroom")
        api_version (str): the version of the API to connect to (ex: "v1")
        *scopes (str[]): a list of permission scopes
        token_path (str): the path to the token.pickle file to use

    Returns:
        A Resource object with methods for interacting with the service.

    """
    print(client_secret_file, api_name, api_version, scopes, token_path, sep='-')
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    cred = None

    # If we already have a token, use that instead of making the user log in
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            print("\ntoken path is: ", token_path, "\n")
            cred = pickle.loads(token.read())

    # If there are no (valid) credentials available, let the user log in.
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
            cred = flow.run_local_server()

        with open('token.pickle', 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(api_name, api_version, credentials=cred)
        print(api_name, 'service created succesfully')
        return service
    except Exception as e:
        print(e)
        return None

def Create_Service_Direct(client_secret_file, api_name, api_version, *scopes, token):
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    try:
        service = build(api_name, api_version, credentials=token)
        print(api_name, 'service created succesfully')
        return service
    except Exception as e:
        print(e)
        return None


def Create_Service_No_Flow(client_secret_file, api_name, api_version, *scopes, driver, secret):
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    cred = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            LOGIN.login()

        with open('token.pickle', 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(api_name, api_version, credentials=cred)
        print(api_name, 'service created succesfully')
        return service
    except Exception as e:
        print(e)
        return None
