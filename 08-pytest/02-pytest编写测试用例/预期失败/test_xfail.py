#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/2/13 15:11

import pytest

version = 5


def add(x, y):
    return x + y


@pytest.mark.xfail()
def test_add_1():
    assert add(2, 2) == 3  # 预期失败，实际失败


@pytest.mark.xfail()
def test_add_2():
    assert add(2, 2) == 4  # 预期失败，实际成功


"""
F:\自动化测试\08-pytest\02-pytest编写测试用例\预期失败>pytest
======================================== test session starts =========================================
platform win32 -- Python 3.8.3, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: F:\自动化测试\08-pytest\02-pytest编写测试用例\预期失败
plugins: allure-pytest-2.9.45
collected 2 items
test_xfail.py xX                                                                                [100%]
=================================== 1 xfailed, 1 xpassed in 0.08s ====================================

"""