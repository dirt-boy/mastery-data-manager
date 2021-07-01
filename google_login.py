"""Google login script."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
