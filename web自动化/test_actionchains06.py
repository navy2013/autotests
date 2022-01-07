# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/22 21:08
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestActionChains():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_action(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, "/html/body/form/input[3]")
        element_right_click = self.driver.find_element(By.XPATH, "/html/body/form/input[4]")
        element_double_click = self.driver.find_element(By.XPATH, "/html/body/form/input[2]")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.click(element_right_click)
        action.click(element_double_click)
        action.perform()

    @pytest.mark.skip
    def test_move(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.XPATH, '//*[@id="dragger"]')
        drop_element = self.driver.find_element(By.XPATH, '/html/body/div[2]')

        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element, drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).perform()
        time.sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.XPATH,'/html/body/label[1]/input')
        ele.click()

        action = ActionChains(self.driver)
        action.send_keys("username").pause(2)
        action.send_keys(Keys.SPACE).pause(2)
        action.send_keys("tom").pause(2)
        action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)


# 执行命令一
if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_actionchains06.py'])

# 执行方式二，在命令行： pytest -s -v test_actionchains06.py
