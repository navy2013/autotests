#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 11:23
import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Main(BasePage):

    def goto_search(self):
        # self.find(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.steps('../page/main.yml')

    def goto_windows(self):
        self.find(By.ID, 'com.xueqiu.android:id/post_status').click()
        time.sleep(6)
        self.find(By.ID, 'tv_search').click()


