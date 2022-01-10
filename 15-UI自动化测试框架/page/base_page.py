#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/10 10:46
import logging

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.wrapper import hander_black


class BasePage:


    def __init__(self, driver:WebDriver = None):
        self._driver = driver

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @hander_black
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement

        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)

        return element


    def find_and_get_text(self, locator, value: str = None):
        element: WebElement
        try:
            if isinstance(locator, tuple):
                element_text = self._driver.find_element(*locator).text
            else:
                element_text = self._driver.find_element(locator, value).text
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element_text
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return self.find_and_get_text(locator, value)
            raise e


