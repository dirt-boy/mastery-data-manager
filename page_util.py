from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
from os import path
import time
import requests
import get_login as creds
import pickle
import sys
sys.path.append('headless-chrome/')
sys.path.append('headless-chrome/chromedriver')
import noviz

driver = noviz.get_driver()
driver.implicitly_wait(10)


def make_name(url):
    name=url[url.rfind('/', 0, url.rfind('/'))+1:url.rfind('/')]
    return name

"""
def get_url():
    url = input('Enter desired URL: ')
    return url
"""

def get_login():
    if path.exists('creds.pickle'):
        login_info=pickle.load( open('creds.pickle', 'rb'))
        print(login_info)
        return login_info
    else:
        credentials = creds.write_creds()
        login_info = pickle.load( open(credentials, 'wb'))
        print(login_info)
        return login_info


def get_page(email, password, url):
    email = email
    password = password
    url = url
    name = make_name(url)
    try:
        
        driver.get(url)
        email_phone = driver.find_element_by_xpath("//input[@id='Email']")
        email_phone.send_keys(email)
        driver.find_element_by_id("next").click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        pwd = driver.find_element_by_xpath("//input[@id='password']")
        pwd.send_keys(password)
        driver.find_element_by_id("submit").click()
        driver.find_element_by_css_selector(".rag0").click()
        pass
    except:
        return None
    time.sleep(5)
    
    html = driver.page_source

    driver.close()

    return html

def prt_scr(name):
    img =driver.save_screenshot(name+'.png')

def get_src(name):
    html = driver.page_source
    with open(name+'.html', 'w') as o:
        o.write(html)


    

    

