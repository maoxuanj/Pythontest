#*- coding:utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["deviceName"] = "Honor 8"
caps["app"] = "C:\\Users\\mxj\\Desktop\\app-my_test-debug.apk"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
time.sleep(3)
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.EditText[1]")
time.sleep(3)
el1.send_keys("15757856712")
time.sleep(3)
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.EditText[2]")
time.sleep(3)
el2.send_keys("mao123456")
time.sleep(3)
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
time.sleep(3)
el3.click()
time.sleep(3)
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[11]/android.widget.LinearLayout/android.widget.ImageView")
time.sleep(3)
el4.click()
time.sleep(3)
