#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/21 22:04

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def setdown(self):
        self.driver.quit()


    def test_hogwards(self):
        self.driver.get("http://www.testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        WebDriverWait()



