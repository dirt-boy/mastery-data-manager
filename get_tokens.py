import os
import pickle
from gAPI import Create_Service
import noviz
import selenium



CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'classroom'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students https://www.googleapis.com/auth/classroom.courses https://www.googleapis.com/auth/classroom.rosters https://www.googleapis.com/auth/classroom.profile.emails https://www.googleapis.com/auth/classroom.rosters']


def read_secret():
	secrets = pickle.load(open('top_secret.pickle', 'rb'))
	return secrets

def delete_token():
	if os.path.exists('token.pickle'):
		os.remove('token.pickle')
	else:
		pass

def gAPI_run(secrets, i):
	svc = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
	driver = hook(secrets, i)
	

def hook(secrets, i):
	#connect to existing chrome instance
	driver = noviz.get_driver()
	url = driver.command_executor._url
	session_id = driver.session_id

	driver = selenium.webdriver.Remote(command_executor=url, desired_capabilities={})
	driver.close()
	driver.session_id = session_id
	login(driver, secrets[i])
	return driver

def login(driver, secret):
	email_phone = driver.find_element_by_xpath("//input[@id='Email']")
	#prt_scr("page2")
	#get_src("page2")
	email_phone.send_keys(secret['email'])
	#prt_scr("page3")
	#get_src("page3")
	driver.find_element_by_id("next").click()
	#prt_scr("page4")
	WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
	#prt_scr("page5")
	pwd = driver.find_element_by_xpath("//input[@id='password']")
	#prt_scr("page6")
	pwd.send_keys(secret['password'])
	#prt_scr("page7")
	driver.find_element_by_id("submit").click()
	WebDriverWait(driver, 5)
	driver.close()

def save_token(tokenlist):
	#save token to new list of tokens
	#read created token.pickle (raw pickle)
	#add to list
	if os.path.exists('token.pickle'):
		with open('token.pickle', 'r') as t:
			tokenlist.append(str(t))
	else:
		pass
	return tokenlist


def get_tokenlist():
	tokens = []
	secrets = read_secret()
	#for each piece of login info in top_secret.py
	for i, s in enumerate(secrets):
		delete_token()
		gAPI_run(secrets, i)
		save_token(tokens)
	return tokens

get_tokenlist()





