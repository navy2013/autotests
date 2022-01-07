#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/4 19:21
import pytest
import yaml

from page.app import App


class TestMain:

    # @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("./test_main.yaml")))
    # def test_main(self, value1, value2):
    def test_main(self):
        app = App()
        app.start().main().goto_search()
        # print(value1)
        # print(value2)

    def test_windows(self):
        app = App()
        app.start().main().goto_windows()



