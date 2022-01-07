#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/23 23:10
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestJs():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_js(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script("document.getElementById('train_date').removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2021-12--01'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))




