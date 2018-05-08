# -*- coding:utf-8 -*-
import os
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import config1
import utils.generator
from log5 import logger
from file_reader import ExcelReader
from utils.HTMLTestRunner_py3 import HTMLTestRunner
from utils.mail import Email
import randomphone
from page.baidu_result_page import BaiDuMainPage, BaiDuResultPage
import logging
logging.basicConfig()

class TestBaiDu(unittest.TestCase):
    URL = config1.Config().get('URL')
    excel = config1.DATA_PATH + '/baidu.xlsx'
    #base_path = os.path.dirname(os.path.abspath(__file__))+ '\..'
    #driver_path = os.path.abspath(base_path+'\chromedriver.exe')
    #5.3 locator_kw = (By.ID, 'kw')
    #5.3locator_su = (By.ID, 'su')
    #5.3 locator_result = (By.XPATH,'//div[contains(@class, "result")]/h3/a')
    #driver =webdriver.Firefox()
    #driver = webdriver.Chrome(executable_path=driver_path)

    def sub_setUp(self):
        #self.driver = webdriver.chrome(executable_path=config1.DRIVER_PATH + '\chromedriver.exe')
        self.driver = webdriver.Firefox()
        self.driver.get(self.URL)
        # 初始页面是main page，传入浏览器类型打开浏览器
        #5.7 self.page = BaiDuMainPage(browser_type='firefox').get(self.URL, maximize_window=True)

    def sub_tearDown(self):
        #5.3self.driver.quit()
        self.page.quit()
    def test_register(self):
        self.sub_setUp()
        self.driver.find_element_by_name('userName').send_keys('15757856712')
        time.sleep(2)
        self.driver.find_element_by_name('password').send_keys('mao123456')
        time.sleep(2)
        self.driver.find_element_by_id('loginBtn').click()
        time.sleep(2)
        #self.driver.maximize_window()
        self.driver.maximize_window()
        # 先定位到搜索输入框
        # 通过id或name定位即可
        self.driver.find_element_by_link_text("贷前管理").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("资信管理").click()
        time.sleep(1)
        self.driver.switch_to_frame('iframe_26')
        ele = self.driver.find_element_by_id("launchedCredit")
        ele.click()
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame('iframe_undefined')
        ele = self.driver.find_element_by_name("customerName")
        cusname = utils.generator.random_name()
        ele.send_keys(cusname)
        shenfen = randomphone.gennerator()
        self.driver.find_element_by_id("cardNo").send_keys(shenfen)
        time.sleep(2)
        Select(self.driver.find_element_by_id("bankDeraler")).select_by_visible_text("工行安徽城建支行")
        time.sleep(2)
        Select(self.driver.find_element_by_id("maritalStatus")).select_by_visible_text("已婚")
        phone = utils.generator.random_phone_number()
        self.driver.find_element_by_name("relavants[0].mobile").send_keys(phone)
        ele = self.driver.find_element_by_id("save")
        ele.click()
        time.sleep(1)
        self.driver.find_element_by_id("sureOption").click()
        time.sleep(2)

        self.driver.find_element_by_xpath("(//input[@name='btSelectItem'])[4]").click()
        self.driver.find_element_by_xpath("(//*[@id='task']/div/div/div[3]/div/button[1])").click()
    '''
    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                time.sleep(5)
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()
    '''
    '''
    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                time.sleep(1)
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()
                              
                a=self.driver.find_element(*self.locator_kw)
                time.sleep(2)
                a.send_keys(d['search'])
                time.sleep(2)
                b=self.driver.find_element(*self.locator_su)
                time.sleep(1)
                b.click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()
                #driver.quit()                
              
                self.page = BaiDuResultPage(self.page)
    '''

    '''
    def search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium+python')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)
            # driver.quit()
    '''
if __name__ == '__main__':
    report = config1.REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(TestBaiDu('test_register'))
    e = Email(title='百度搜索测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='1551660491@qq.com',
              server='smtp.163.com',
              sender='maoxuanjie25@163.com',
              password='mao123456',
              path=report
              )
    e.send()