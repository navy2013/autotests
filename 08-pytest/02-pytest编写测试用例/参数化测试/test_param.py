#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/2/13 15:22

import pytest

@pytest.mark.parametrize("name", ["Mark", "Joe"])
def test_use_param(name):
    assert name == "Mark"


"""
F:\自动化测试\08-pytest\02-pytest编写测试用例\参数化测试>pytest
======================================== test session starts =========================================
platform win32 -- Python 3.8.3, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: F:\自动化测试\08-pytest\02-pytest编写测试用例\参数化测试
plugins: allure-pytest-2.9.45
collected 2 items                                                                                     

test_param.py .F                                                                                [100%]

============================================== FAILURES ==============================================
________________________________________ test_use_param[Joe] _________________________________________

name = 'Joe'

    @pytest.mark.parametrize("name", ["Mark", "Joe"])
    def test_use_param(name):
>       assert name == "Mark"
E       AssertionError: assert 'Joe' == 'Mark'
E         - Mark
E         + Joe

test_param.py:10: AssertionError
====================================== short test summary info =======================================
FAILED test_param.py::test_use_param[Joe] - AssertionError: assert 'Joe' == 'Mark'
==================================== 1 failed, 1 passed in 0.08s =====================================

"""
