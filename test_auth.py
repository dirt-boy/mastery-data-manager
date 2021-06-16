from google.oauth2 import id_token
from google.auth.transport import requests
import pickle


CLIENT_ID = "604190966773-cuu4vfglal0b1dr1rg6mlh2bfjntch9u.apps.googleusercontent.com"
# (Receive token by HTTPS POST)
# ...

token = pickle.loads(open("data/tokens/token_admin.pickle", "rb").read())

    # Specify the CLIENT_ID of the app that accesses the backend:
print(eval(token))
idinfo = id_token.verify_oauth2_token(token, requests.Request())

# Or, if multiple clients access the backend server:
# idinfo = id_token.verify_oauth2_token(token, requests.Request())
# if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
#     raise ValueError('Could not verify audience.')

# If auth request is from a G Suite domain:
# if idinfo['hd'] != GSUITE_DOMAIN_NAME:
#     raise ValueError('Wrong hosted domain.')

# ID token is valid. Get the user's Google Account ID from the decoded token.
print("got this far")
userid = idinfo['sub']
print(userid)