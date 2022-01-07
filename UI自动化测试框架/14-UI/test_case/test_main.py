#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 11:29
from page.app import App


class TestMain:

    def test_search(self):
        app = App()
        app.start().main().goto_search()



