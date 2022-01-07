# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/23 0:53
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get('https://ssl.zc.qq.com/v3/index-chs.html')
        self.driver.find_element(By.XPATH,'//*[@id="nickname"]').send_keys('fajafjl')
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('123')
        self.driver.find_element(By.XPATH,'//*[@id="phone"]').send_keys('18677772222')
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/form/div[8]/label')
        self.driver.find_element(By.XPATH,'//*[@id="get_acc"]').click()
        time.sleep(3)
