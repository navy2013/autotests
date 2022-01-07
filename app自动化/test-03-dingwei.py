#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/12/12 17:26

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='127.0.0.1:7555'
desired_caps['appPackage']='com.xueqiu.android'
desired_caps['appActivity']='com.xueqiu.android.common.MainActivity'
desired_caps['noReset'] = 'true'
desired_caps['dontStopAppOnReset'] = 'true'
desired_caps['skipDeviceInitialization'] = 'true'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)
el1 = driver.find_element(By.ID, "com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
el2.send_keys("阿里巴巴")
driver.back()
driver.back()

driver.quit()


