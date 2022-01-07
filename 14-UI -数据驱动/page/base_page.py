#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 10:48
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        return self._driver.find_element(locator, value)

    def steps(self, path):
        with open(path, 'r') as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if 'by' in step.keys():
                element = self.find(step['by'], step['locator'])
            if 'action' in step.keys():
                action = step['action']
                if action == 'click':
                    element.click()

