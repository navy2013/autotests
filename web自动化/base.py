# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/23 22:43
import os
from selenium import webdriver


class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
