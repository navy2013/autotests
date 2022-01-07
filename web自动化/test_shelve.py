# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/30 20:59

"""
利用cookie，登录企业微信，点击通讯录
"""
import shelve

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestShelve():
    def setup(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open('cookies')
        # db['cookies'] = self.driver.get_cookies()
        cookies = db['cookies']
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.ID, 'menu_contacts').click()
