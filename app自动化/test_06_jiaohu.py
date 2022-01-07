#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/12/18 22:33
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestJiaohu:
    def setup(self):
        caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'deviceName': '31ac524b',
            'appPackage': 'com.xueqiu.android',
            'appActivity': 'com.xueqiu.android.common.MainActivity',
            'unicodeKeyBoard': 'true',
            'resetKeyBoard': 'true',
            'udid': '31ac524b',
            'noReSet': 'true'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_mobile(self):
        self.driver.make_gsm_call('18679111547', GsmCallActions.CALL)
        self.driver.send_sms('13214577788', 'hello appium api')
