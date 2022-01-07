# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/22 23:30
import pytest
import time
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction():
    """
    打开chrome
    打开url：http://www.baidu.com
    向搜索框中输入‘selenium测试’
    通过TouchAction点击搜索框
    滑动到底部，点击下一页
    关闭Chrome
    """

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touch_action(self):
        self.driver.get("http://www.baidu.com")
        input = self.driver.find_element(By.XPATH, '//*[@id="kw"]')

        input.send_keys('selenium测试')

        # el_search = self.driver.find_element_by_xpath('//*[@id="su"]')
        # # el.clear()
        # el.send_keys('selenium测试')
        #
        # action = TouchActions(self.driver)
        # action.tap(el_search)
        # action.perform()
        #
        # action.scroll_from_element(el, 0, 10000).perform()
        # time.sleep(3)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_touchchains.py'])
