#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 10:53
import yaml
from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {}
            # caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = yaml.safe_load(open("../page/configuration.yml"))["caps"]["deviceName"]
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            # 初始化driver
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(3)
        return self

    def main(self) -> Main:
        return Main(self._driver)
