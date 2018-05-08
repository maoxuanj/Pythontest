"""
# -*- coding:utf-8  -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://www.baidu.com"
base_path = os.path.dirname(os.path.abspath(_file_))+'\..'
driver_path =os.path.abspath(base_path+'\driver\chormedriver.exe')
locator_kw = (By.ID,'kw')
locator_su = (By.ID,'su')
locator_result = (By.XPATH,'//div[contains@class,"result"]/h3/a')
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(URL)
driver.find_element(*locator_kw).send_keys('selenium')
dirver.find_element(*locator_su).click()
time.sleep(2)
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)
driver.quit()
"""

# -*- coding:utf-8 -*-
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import config1
URL = "http://www.baidu.com"
##base_path = os.path.dirname(os.path.abspath(__file__))+ '\..'
##driver_path = os.path.abspath(base_path+'\chromedriver.exe')
driver = webdriver.Firefox()
driver.get(URL)
locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
locator_result = (By.XPATH,'//div[contains(@class, "result")]/h3/a')
##driver = webdriver.Chrome(executable_path=driver_path)
def set_up(self):
    driver.get(URL)
def search_0(self):
    driver.find_element(*locator_kw).send_keys('selenium')
    driver.find_element(*locator_su).click()
    time.sleep(2)
    links = driver.find_elements(*locator_result)
    for link in links:
        print(link.text)
    #driver.quit()
def search_1(self):
    driver.find_element(*locator_kw).send_keys('selenium+python')
    driver.find_element(*locator_su).click()
    time.sleep(2)
    links = driver.find_elements(*locator_result)
    for link in links:
        print(link.text)
        # driver.quit()
if __name__ == '__main__':
    unittest.main()



