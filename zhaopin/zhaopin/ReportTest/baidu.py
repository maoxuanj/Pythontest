# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchAttributeException
import unittest, time, re
import HTMLTestRunner
import random


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu_search(self):
        u"""百度搜索"""
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    def test_baidu_set(self):
        u"""百度设置"""
        driver = self.driver
        # 进入搜索设置页
        driver.get(self.base_url + '/gaoji/preferences.html')
        # 设置每页搜索结果为 20 条
        m = driver.find_element_by_name("NR")
        m.find_element_by_xpath("//option[@value='20']").click()
        time.sleep(2)
        # 保存设置的信息
        driver.find_element_by_xpath("/html/body/form/div/input").click()
        time.sleep(2)
        driver.switch_to_alert().accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        if __name__ == "__main__":
            unittest.main()

