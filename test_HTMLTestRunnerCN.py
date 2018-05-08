# -*- coding:utf-8 -*-
__author__='MXJ'
import unittest
import HTMLTestRunnerCN
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys #需要引入keys包
from selenium.webdriver.support.ui import Select
import randomphone
import random
import string
import win32gui
import win32con
import time
import SendKeys

driver = webdriver.Firefox()
#测试用例

class creditTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testCase1(self):
        #登入case
        driver.get("http://192.168.10.204:8080/view/main.html")
        ele = driver.find_element_by_name("userName")
        ele.send_keys("15757856712")
        ele = driver.find_element_by_name("password")
        ele.send_keys("mao123456")
        ele = driver.find_element_by_id("loginBtn")
        ele.click()
        sleep(1)
        print "浏览器最大化成功！"
        driver.maximize_window()


    def testCase2(self):
        #进入征信发起
        driver.maximize_window()
        sleep(1)
        # 先定位到搜索输入框
        # 通过id或name定位即可
        driver.find_element_by_link_text("贷前管理").click()
        sleep(1)
        driver.find_element_by_link_text("资信管理").click()
        sleep(1)
        driver.switch_to_frame('iframe_26')
        ele = driver.find_element_by_id("launchedCredit")
        ele.click()
        sleep(2)
        print "进入征信发起页面！"

    def testCase3(self):
        #生成随机姓名与证件号
        driver.switch_to.default_content()
        driver.switch_to_frame('iframe_undefined')
        ele = driver.find_element_by_name("customerName")
        shenfen = randomphone.gennerator()
        name = randomphone.randomname1()
        driver.find_element_by_id("cardNo").send_keys(shenfen)
        # driver.find_element_by_id("cardNo").send_keys("5646132")  固定输入，验证alert
        Select(driver.find_element_by_id("bankDeraler")).select_by_visible_text(u"工行安徽城建支行")
        Select(driver.find_element_by_id("maritalStatus")).select_by_visible_text("未婚")
        phone = randomphone.createPhone()
        driver.find_element_by_name("relavants[0].mobile").send_keys(phone)
        sleep(1)
        driver.find_element_by_name("customerName").send_keys(name)
        print "客户生成成功！"
        sleep(3)
    def testCase4(self):
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        # SendKeys
        SendKeys.SendKeys("C:\\Users\\mxj\\Desktop\\error\\timg1.jpg")
        sleep(2)
        SendKeys.SendKeys("{ENTER}")
        sleep(2)
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        # SendKeys
        SendKeys.SendKeys("C:\\Users\\mxj\\Desktop\\error\\shensu2016052301[1].jpg")
        sleep(2)
        SendKeys.SendKeys("{ENTER}")
        sleep(2)
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        # SendKeys
        SendKeys.SendKeys("C:\\Users\\mxj\\Desktop\\error\\7.1.png")
        SendKeys.SendKeys("{ENTER}")
        print "上传照片成功！"
    def testCase5(self):
        sleep(2)
        driver.find_element_by_name("estimateLoanAmount").clear()
        driver.find_element_by_name("estimateLoanAmount").send_keys("100000")
        sleep(1)
        ele = driver.find_element_by_id("save")
        ele.click()
        sleep(1)
        driver.find_element_by_id("sureOption").click()
        sleep(2)
        driver.find_element_by_xpath("(//input[@name='btSelectItem'])[4]").click()
        driver.find_element_by_xpath("(//*[@id='task']/div/div/div[3]/div/button[1])").click()
        print "征信发起提交成功！"
    def testCase6(self):
        sleep(5)
        driver.switch_to.default_content()
        # driver.find_element_by_css_selector("span.nav-label").click()
        sleep(5)
        driver.find_element_by_link_text("我的任务").click()
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'我的任务')]").click()
        # driver.switch_to.default_content()
        driver.switch_to_frame('iframe_21')
        sleep(3)
        s1 = driver.find_element_by_id("ftCode")
        Select(s1).select_by_value("CREDIT_FLOW")
        driver.find_element_by_css_selector("option[value=\"CREDIT_FLOW\"]").click()
        Select(driver.find_element_by_id("flowNode")).select_by_visible_text("征信接受")
        driver.find_element_by_id("btn-search").click()
        sleep(2)
        driver.find_element_by_link_text("征信接受").click()
        sleep(1)
        driver.switch_to.default_content()
        driver.switch_to_frame('iframe_undefined')
        sleep(2)
        driver.find_element_by_id("save").click()
        sleep(2)
        driver.find_element_by_id("sureOption").click()
        sleep(2)
        print "征信流程完成！"
class APITestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCase1(self):
        self.assertEqual(2, 2, "testError")

    def testCase2(self):
        self.assertEqual(3, 3, "testError")

    def testCase3(self):
        self.assertEqual(5, 5, "testError")

    def testCase4(self):
        self.assertEqual(2, 1, "测试错误")

    def testCase5(self):
        self.assertEqual(2, 9, "testError")

    def testCase6(self):
        pass

#添加Suite
def Suite():
    #定义一个单元测试容器
    suiteTest = unittest.TestSuite()
    #将测试用例加入到容器
    suiteTest.addTest(creditTestCase("testCase1"))
    suiteTest.addTest(creditTestCase("testCase2"))
    suiteTest.addTest(creditTestCase("testCase3"))
    suiteTest.addTest(creditTestCase("testCase4"))
    suiteTest.addTest(creditTestCase("testCase5"))
    suiteTest.addTest(creditTestCase("testCase6"))
    suiteTest.addTest(APITestCase("testCase1"))
    suiteTest.addTest(APITestCase("testCase2"))
    suiteTest.addTest(APITestCase("testCase3"))
    suiteTest.addTest(APITestCase("testCase4"))
    suiteTest.addTest(APITestCase("testCase5"))
    suiteTest.addTest(APITestCase("testCase6"))
    return suiteTest

'''
问题：代码写的没问题，执行也成功了，但就是无法生成HTMLTestRunner的报告
其实这是编辑器搞得鬼，编辑器为了方便用户执行测试，都有一项功能，可以用编辑器来调用unittest或者nose来执行测试用例，这种情况下，执行的只是用例或者套件，而不是整个文件，写在main里的代码是不会被执行的！！自然无法生成测试报告
我们在如果想要生成测试报告，那么一定要注意右键执行时选择的右键菜单，一定要当做文件执行，不要让编辑器当做用例执行
if __name__ == ‘__main__‘:
if __name__ == ‘python‘:
# 把main修改成自己的文件夹名就可以了
---试了不行
'''
if __name__ == '__main__':
    #确定生成报告的路径
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    filePath ='D:\\report\\HTMLTestRunnerCN'+rq+'.html'

    fp = file(filePath,'wb')
    #生成报告的Title,描述
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        #description='详细测试用例结果',
        tester=u"Findyou"
        )
    #运行测试用例
    runner.run(Suite())
    # 关闭文件，否则会无法生成文件
    #fp.close()