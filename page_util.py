"""
Handles Google account login through headless Chrome instance created by noviz.py
"""

import pickle
import sys
import time
from os import path

import get_login as creds
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
    #add exception for invalid login!!!
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
        #prt_scr("page1")
        email_phone = driver.find_element_by_xpath("//input[@id='Email']")
        #prt_scr("page2")
        #get_src("page2")
        email_phone.send_keys(email)
        #prt_scr("page3")
        #get_src("page3")
        driver.find_element_by_id("next").click()
        #prt_scr("page4")
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        #prt_scr("page5")
        pwd = driver.find_element_by_xpath("//input[@id='password']")
        #prt_scr("page6")
        pwd.send_keys(password)
        #prt_scr("page7")
        driver.find_element_by_id("submit").click()
        prt_scr("page8")
        #get_src("page8")
        html = driver.page_source
        driver.find_element_by_css_selector(".rag0").click()
        prt_scr("page9")
        #get_src("page9")
        pass
    except:
        pass
    time.sleep(5)

    #prt_scr(str(url))
    html = driver.page_source


    return html

def end_session():
    driver.quit()

def prt_scr(name):
    img =driver.save_screenshot(name+'.png')

def get_src(name):
    html = driver.page_source
    with open(name+'.html', 'w') as o:
        o.write(html)