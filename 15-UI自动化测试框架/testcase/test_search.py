#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/10 12:20
import time

from page.app import App


class TestSearch():
    def setup(self):
        # 进入搜索页
        self.search = App().start().main().goto_market().goto_search()

    def test_search(self):
        self.search.search("阿里巴巴-SW")
        assert self.search.is_choose("阿里巴巴-SW")


