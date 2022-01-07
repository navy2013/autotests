# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/24 22:29
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAlert():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        drag = self.driver.find_element(By.XPATH, '//*[@id="draggable"]')
        drop = self.driver.find_element(By.XPATH, '//*[@id="droppable"]')

        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '//*[@id="submitBTN"]')
        time.sleep(3)



