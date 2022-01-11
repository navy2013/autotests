# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/10 12:00
import yaml
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Search(BasePage):
    def search(self, name):
        # self.find(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys("alibaba")
        # self.find(By.XPATH, '//*[@text="BABA"]').click()
        # print("BABA")
        # self.find(By.XPATH, '//*[@text="股票"]').click()
        # print("股票")
        # self.find(By.XPATH, f'//*[@resource-id="com.xueqiu.android:id/item_stock"]//*[@text="{name}"]/../..//*[@text="加自选"]').click()
        self._params["name"] = name
        self.step("../page/search.yaml")

    def add(self, name):
        self._params["name"] = name
        self.step("../page/search.yaml")

    def is_choose(self, name):
        # eles = self.finds(By.XPATH, f'//*[@resource-id="com.xueqiu.android:id/item_stock"]//*[@text="{name}"]/../..//*[@text="已添加"]')
        # return len(eles) > 0
        self._params["name"] = name
        return self.step("../page/search.yaml")

    def reset(self, name):
        self._params["name"] = name
        self.step("../page/search.yaml")
