#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/12/8 22:02

from appium import webdriver
desc = {}
# 设备类型
desc['platformName'] = 'Android'
# 设备型号
desc['platformVersion'] = '6.0'
# 设备名
desc['deviceName'] = 'emulator-5554'
# 包名
desc['appPackage'] = 'com.android.settings'
# 启动入口
desc['appActivity'] = 'com.android.settings.Settings'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desc)
driver.quit()





