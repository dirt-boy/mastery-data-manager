"""
Handles Google account login through headless Chrome instance created by noviz.py
"""

import pickle
import sys
import time
#probably don't need getpass?
#since its grabbing them from a file... and in any kind of webapp it'd have to be a totally different module
import getpass
from os import path

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

#import get_login as creds



from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

sys.path.append('headless-chrome/')
sys.path.append('headless-chrome/chromedriver')

CREDPATH = "data/logins"

def get_creds():
        file = open(CREDPATH, "r")
        creds = json.loads(file.read())
        return creds

class Creds:

    def __init__(self, creds):
        self.creds = (get_creds())




def noviz():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.binary_location = 'chromedriver'
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    #driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver_unix'), chrome_options=chrome_options)
    return driver

driver = noviz.get_driver()
driver.implicitly_wait(10)
ceds = Creds()

def make_name(url):
    name=url[url.rfind('/', 0, url.rfind('/'))+1:url.rfind('/')]
    return name


def readsrc(token, url):
    login = creds[token]
    html = get_page(*login, url)
    #test
    #print(html)
    with open('submission.html', 'w') as o:
        o.write(html)  


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
        html = driver.page_source
        driver.find_element_by_css_selector(".rag0").click()
        pass
    except:
        pass
    time.sleep(5)
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