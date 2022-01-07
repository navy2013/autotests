#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 11:23
import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Main(BasePage):

    def goto_search(self):
        self.find(By.ID, 'com.xueqiu.android:id/tv_search').click()
        time.sleep(3)


