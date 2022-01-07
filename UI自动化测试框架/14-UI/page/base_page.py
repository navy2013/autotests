#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 10:48
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        self._driver.find_element(locator, value)


