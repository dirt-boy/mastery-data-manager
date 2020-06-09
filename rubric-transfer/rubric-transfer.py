import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#this will copy all text (including tables) from single rubric
#must still implement foreach thru folder -> find elem with text "Rubric"

class TestCopypasterubric():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_copypasterubric(self):
    self.driver.get("https://docs.google.com//document/d/1Soqfsqr2HPOU6OzGxcHrBIEv06UKnFwdHz99Ia4VEjA/edit")
    self.driver.find_element(By.ID, "docs-edit-menu").click()
    self.driver.find_element(By.CSS_SELECTOR, "#\\3A bk .goog-menuitem-label").click()
    self.driver.get("https://sheets.google.com")

#add in python script for pasting into google sheets




