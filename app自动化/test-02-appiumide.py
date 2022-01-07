# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/12/12 16:24

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from selenium.webdriver.common.by import By

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "127.0.0.1:7555 "
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["ensureWebviewsHavePages"] = True
caps["nativeWebScreenshot"] = True
caps["chromeOptions"] = {"w3c":"false"}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element(By.ID, "com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
el2.send_keys("阿里巴巴")
el3 = driver.find_element(By.XPATH,
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
el3.click()

driver.quit()
