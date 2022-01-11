#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/10 11:59
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.search import Search


class Market(BasePage):
    def goto_search(self):
        # 点击行情页_搜索框，进入搜索页
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        print("行情页--------")
        return Search(self._driver)


