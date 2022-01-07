#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/24 21:35
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFiles():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_files(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="sttb"]/img[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="stuurl"]').send_keys('https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F813bc78319d4b663ba4783190b3d2c91838e014e1e41f-G8Ch87_fw658&refer=http%3A%2F%2Fhbimg.b0.upaiyun.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1640353250&t=eb979e6515ae821fc36ca5e2ac9b6170')
        time.sleep(3)



