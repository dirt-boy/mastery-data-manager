import getpass
import pickle

def get_creds():
    email = input("email:")
    password = getpass.getpass(prompt="password:")
    return [email, password]

def write_creds():
    with open('creds.pickle', 'x') as creds:
        credfile = pickle.dump(get_creds(), creds)
        print(credfile)
    return credfile


