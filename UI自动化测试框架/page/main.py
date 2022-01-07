#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/4 19:18
from page.base_page import BasePage
from selenium.webdriver.common.by import By

class Main(BasePage):
    def goto_search(self):
        # self.find(By.ID, "tv_search").click()
        self.steps("../page/main.yaml")

    def goto_windows(self):
        self.find(By.ID, "post_status").click()
        self.find(By.ID, "tv_search").click()


