# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/10 11:58
import time

import yaml
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.market import Market


class Main(BasePage):
    def goto_market(self):
        # 点击首页_详情,进入行情页
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        # time.sleep(3)
        self.set_implicitly(10)
        self.step("../page/main.yaml")
        self.set_implicitly(3)
        return Market(self._driver)
