#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/10 12:20
import time

import pytest
import yaml

from page.app import App


class TestSearch():
    def setup(self):
        # 进入搜索页
        self.search = App().start().main().goto_market().goto_search()

    # @pytest.mark.parametrize("name", ["阿里巴巴-SW", "阿里巴巴"])
    @pytest.mark.parametrize("name", yaml.safe_load(open("../testcase/test_search.yaml", encoding="utf-8") ))
    def test_search(self, name):
        # if self.search.is_choose("阿里巴巴-SW"):
        #     time.sleep(3)
        #     self.search.reset("阿里巴巴-SW")
        # name = "阿里巴巴-SW"
        self.search.search(name)
        if self.search.is_choose(name):
            self.search.reset(name)
        self.search.add(name)
        assert self.search.is_choose(name)


