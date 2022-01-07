#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/23 21:16
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWindows():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.LINK_TEXT, '登录').click()
        # print(self.driver.current_window_handle)
        self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]').send_keys('南航海军上校')
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]').send_keys('南航海军上校')
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]').send_keys('fajjf')
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__submit"]').click()
        time.sleep(20)



