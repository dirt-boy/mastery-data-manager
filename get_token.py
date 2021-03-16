"""Gets the OAuth token."""
import getpass
import os
import shutil

import gAPI as g

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses https://www.googleapis.com/auth/classroom.rosters https://www.googleapis.com/auth/classroom.profile.emails https://www.googleapis.com/auth/classroom.rosters']

g.Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

#move token.pickle to data/tokens

def save_token(dest, file, file_new):
	save_path = dest+ '/data/tokens/'+file_new
	curr_path = dest+'/'+file
	shutil.move(curr_path, save_path)

#username used as unique identifier for token
sfx = str(getpass.getuser())
token_orig = 'token.pickle'
token_new = 'token_'+sfx+'.pickle'
token_path = os.path.dirname(os.path.abspath(token_orig))

save_token(token_path, token_orig, token_new)
