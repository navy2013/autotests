#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/7 23:53

import pytest

@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",30)])
def test_eval(test_input,expected):
    assert eval(test_input) == expected


