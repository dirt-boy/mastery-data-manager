from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from collections import ChainMap
import requests

def save_cookies():
    email = "classroom.admin@codenation.org"
    password = "e4a4eefee975"
    url = "https://classroom.google.com/u/0/c/MTE0NTcxNDk1Mzgz/a/MTE0NTcxNDk1Mzkx/details"
    driver = webdriver.Chrome()
    driver.get(url)
    email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
    email_phone.send_keys(email)
    driver.find_element_by_id("identifierNext").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
    pwd = driver.find_element_by_xpath("//input[@name='password']")
    pwd.send_keys(password)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(5)

    g_cookies = driver.get_cookies()
    
    names = []
    values = []
    

    for cookie in g_cookies:
        names.append(cookie['name'])
        values.append(cookie['value'])
    
    cookies = dict(zip(names, values))

    return cookies


def set_params(url, cookies, headers, files, cookies):
cookies = save_cookies()
url = "https://classroom.google.com/u/1/v7/rubric/list?_reqid=684545&rt=j"
payload = {'f.req': '[[null,[["52609649719","102616360750"]]]]',
'token': 'ABFGqemQrjMFXA3O5fs39DRRATi_wxbNow:1591663228646'}
files = []
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
  'Authorization': 'Bearer ya29.a0AfH6SMCgCyleO0o2MS0Gu8rryJyYYkT-PKKmPENFPYWTgjL6cjrlOzhG_ebyH5rmiQACLPIgyz59sxqdvGqhe77vAXEQIc96ucK295-2TiDD6XV2DAE22b4NsEp9dsw7BP4QIE5MwhSaPi6cdoogfGzXPcUG5My1OV8'}

set_params("https://classroom.google.com/u/1/v7/rubric/list?_reqid=684545rt=j",['f.req': '[[null, [["52609649719". "102616360750"]]]]', 'token':'ABFGgemQrjMFXA305Fs39DRRATi_wxbNow:1591663228646'}, files=[], headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML,     like Gecko) Chrome/83.0.4103.97 Safari/537.36',
 48   'Authorization': 'Bearer ya29.a0AfH6SMCgCyleO0o2MS0Gu8rryJyYYkT-                              PKKmPENFPYWTgjL6cjrlOzhG_ebyH5rmiQACLPIgyz59sxqdvGqhe77vAXEQIc96ucK295-                2TiDD6XV2DAE22b4NsEp9dsw7BP4QIE5MwhSaPi6cdoogfGzXPcUG5My1OV8'}

def try-post():
    response = requests.request("POST", url, headers=headers, data = payload, files = files, cookies=cookies)
    print('cookies sent:', cookies)
    print('headers sent:', headers)
    print('payload sent:', payload)
    print(response.text)
