from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from collections import ChainMap
import requests
import getpass

def make_name(url):
    name=url[url.rfind('/', 0, url.rfind('/'))+1:url.rfind('/')]
    return name
    
def get_login():
    print("Enter Classroom Admin Email:")
    email=input()
    print('\n')
    print("Enter Classroom Admin Password:")
    pwd = getpass.getpass(prompt="Password:")
    return [email, pwd]

def get_page(email, password, url):
    email = email
    password = password
    url = url
    name = make_name(url)
    print(name)
    driver = webdriver.Chrome()
    driver.get(url)
    email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
    email_phone.send_keys(email)
    driver.find_element_by_id("identifierNext").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
    pwd = driver.find_element_by_xpath("//input[@name='password']")
    pwd.send_keys(password)
    driver.find_element_by_id("passwordNext").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rag0")))
    driver.find_element_by_css_selector(".rag0").click()
    time.sleep(5)

    html = driver.page_source

    with open(name+'.html', 'w') as o:
       file=o.write(html)
    return file
    
    #g_cookies=driver.get_cookies()


    """
    g_cookies=[]
    g_cookies.append(driver.get_cookie('SID'))
    g_cookies.append(driver.get_cookie('__Secure-3PSID'))
    """

    """
    cookies={}
    for cookie in g_cookies:
        cookies
    """
    #return g_cookies

"""
def set_params(url, data, headers,files, cookies):
    url = url
    files = files
    headers = headers
    return [url, data, headers,files, cookies]

params = set_params("https://classroom.google.com/u/1/v7/rubric/list?_reqid=684545&rt=j",
        {'f.req': '[[null,[["52609649719","102616360750"]]]]',
'token': 'ABFGqemQrjMFXA3O5fs39DRRATi_wxbNow:1591663228646'}, 
        {'X-Same-Domain': '1','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36','Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Accept':'*/*','Authorization': 'Bearer ya29.a0AfH6SMCgCyleO0o2MS0Gu8rryJyYYkT-PKKmPENFPYWTgjL6cjrlOzhG_ebyH5rmiQACLPIgyz59sxqdvGqhe77vAXEQIc96ucK295-2TiDD6XV2DAE22b4NsEp9dsw7BP4QIE5MwhSaPi6cdoogfGzXPcUG5My1OV8'}, [], save_cookies())

def sel_post(url, payload={}, headers={}, files=[], cookies=[]):
    s = requests.Session()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])
    s.headers = headers
    response = s.post(url, data=payload, files=files)
    request_obj = response.request
    print('\n')
    print('HEADERS:\n', request_obj.headers, '\n')
    print('BODY:\n', request_obj.body, '\n')
    #print(request_obj.method)
    #print(request_obj.url)
    print('RESPONSE:\n', response.text,'\n')


def pprint_POST(req):
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

def dl_page():
    html = driver.page_source()
    with open('output.html', 'w') as o:
        o.write(html)



#pprint_POST(sel_post(*params))

#sel_post(*params)
"""
