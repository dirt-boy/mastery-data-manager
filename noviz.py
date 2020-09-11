import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  

def get_driver():

    chrome_options = Options()  
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.binary_location = 'chromedriver'
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver_osx'), chrome_options=chrome_options)
    #driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver_unix'), chrome_options=chrome_options)
    return driver
