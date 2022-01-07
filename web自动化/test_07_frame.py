# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/23 22:29
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFrame():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        # self.driver.switch_to_frame('iframeResult')
        print(self.driver.find_element(By.XPATH, '//*[@id="draggable"]').text)
        self.driver.switch_to.default_content()
        # self.driver.switch_to.parent_frame()
        print(self.driver.find_element(By.XPATH, '//*[@id="submitBTN"]').text)
        time.sleep(3)