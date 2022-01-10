# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/10 11:58
import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.market import Market


class Main(BasePage):
    def goto_market(self):
        # 点击首页_详情,进入行情页
        self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        time.sleep(3)
        return Market(self._driver)
