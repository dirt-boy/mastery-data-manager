import getpass
import pickle

def get_creds():
    email = input("email:")
    password = getpass.getpass(prompt="password:")
    return [email, password]

def write_creds():
    with open('creds.pickle', 'wb+') as creds:
        cred_r = get_creds()
        print("cred_r: "+str(cred_r)+"\n")
        print("creds: "+ str(creds)+"\n")
        credfile = pickle.dump(cred_r, creds)
        print(credfile)
    return credfile


