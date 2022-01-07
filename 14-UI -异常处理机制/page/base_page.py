# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 10:48
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver
    _black_list = [(By.ID, 'iv_close')]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            print("开始处理黑名单")
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()  # 取0是因为每次只能有一个弹窗
                    break
            print("处理黑名单", black)
            # 处理完黑名单后，再次找原来的元素
            return self.find(locator, value)

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
