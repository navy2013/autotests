#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 15:59
from page.app import App


class TestBase:
    app = None

    def setup(self):
        self.app = App()


