#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/12/31 20:44
from time import sleep

import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver


class TestXueQiu:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = '127.0.0.1:7555'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['noReset'] = 'true'
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        print("teardown")
        self.driver.quit()

    # def setup(self):
    #     print("setup")
    #     pass
    #
    # def teardown(self):
    #     print("teardown")
    #     self.driver.find_element(MobileBy.ID, 'com.xueqiu.android')

    # @pytest.mark.parametrize('searchkey', 'searchresult', [('alibaba', '阿里巴巴'), ('jd', '京东')])
    def test_search(self):
        print("search")
        el1 = self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/tv_search')
        el1.click()

        el2 = self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')


        el3 = self.driver.find_element(MobileBy.XPATH, '//*[@text="BABA"]')
        el3.click()

        el4 = self.driver.find_element(MobileBy.XPATH, '//*[@text="加自选"]')
        el4.click()
        sleep(5)




