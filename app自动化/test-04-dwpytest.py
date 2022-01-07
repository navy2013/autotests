#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/12/12 20:50

#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/12/12 17:26
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

class TestDw:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='6.0'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']='com.xueqiu.android'
        desired_caps['appActivity']='com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    @pytest.mark.skip()
    def test_search(self):
        print("搜索测试用例")
        el1 = self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        ele3 = self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        ele3.click()
        current_price = float(self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/current_price"]').text)
        assert current_price < 200

    @pytest.mark.skip()
    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_get_current(self):
        el1 = self.driver.find_element(By.ID, "com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        ele3 = self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        ele3.click()
        current_price = self.driver.find_element(By.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前09988 对应的股票价格: {current_price}")
        assert float(current_price) < 200


if __name__ == '__main__':
    pytest.main()


