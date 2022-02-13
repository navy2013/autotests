#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/2/13 15:28

import pytest

name_age = [("Mark", 18),("Joe", 20)]

@pytest.mark.parametrize("name,age",name_age)
def test_use_param(name,age):
    assert name == "Mark" and age == 18



"""
F:\自动化测试\08-pytest\02-pytest编写测试用例\参数化测试>pytest test03_param.py
======================================== test session starts =========================================
platform win32 -- Python 3.8.3, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: F:\自动化测试\08-pytest\02-pytest编写测试用例\参数化测试
plugins: allure-pytest-2.9.45
collected 2 items                                                                                     

test03_param.py .F                                                                              [100%]

============================================== FAILURES ==============================================
_______________________________________ test_use_param[Joe-20] _______________________________________

name = 'Joe', age = 20

    @pytest.mark.parametrize("name,age",name_age)
    def test_use_param(name,age):
>       assert name == "Mark" and age == 18
E       AssertionError: assert ('Joe' == 'Mark'
E         - Mark
E         + Joe)

test03_param.py:12: AssertionError
====================================== short test summary info =======================================
FAILED test03_param.py::test_use_param[Joe-20] - AssertionError: assert ('Joe' == 'Mark'
==================================== 1 failed, 1 passed in 0.08s =====================================

"""