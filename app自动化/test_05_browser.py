#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/12/15 23:14

from appium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'browserName': 'Browser',
            'noReset': True,
            'deviceName': '127.0.0.1:7555',
            'chromedriverExecutable': 'C:/Users/navy/AppData/Local/Programs/Appium/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win/chromedriver_win32_v2.40.exe'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        click_locator = (By.ID,'index-kw')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(click_locator))
        self.driver.find_element(By.ID, 'index-kw').click()
        self.driver.find_element(By.ID, 'index-kw').send_keys('appium')

        search_locator = (By.ID, 'index-bn')
        self.driver.find_element(*search_locator).click()



