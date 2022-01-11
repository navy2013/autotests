#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/10 10:46
import inspect
import json

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.wrapper import hander_black


class BasePage:
    _params = {}

    def __init__(self, driver:WebDriver = None):
        self._driver = driver

    def set_implicitly(self, time):
        self._driver.implicitly_wait(time)

    def screenshot(self, name):
        self._driver.save_screenshot(name)

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @hander_black
    def find(self, locator, value: str = None):
        element: WebElement

        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)

        return element

    @hander_black
    def find_and_get_text(self, locator, value: str = None):
        element: WebElement

        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text

    def step(self, path):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function  # 0：获取自身函数名 1：获取最近一层调用的函数名 2：获取最近二层调用的函数名
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            # raw = raw.replace(f"{{{key}", value)
            raw = raw.replace('${' +key+ '}', value)
        steps = json.loads(raw)
        for step in steps:
            element = None
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    self.find(step["by"], step["locator"]).click()
                if action == "send":
                    value = step["value"]
                    self.find(step["by"], step["locator"]).send_keys(value)
                if action == "len > 0":
                    eles = self.finds(step["by"], step["locator"])
                    return len(eles) > 0