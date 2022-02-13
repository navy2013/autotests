#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/2/13 15:25

import pytest

@pytest.mark.parametrize("name", ["Mark", "Joe"])
@pytest.mark.parametrize("age", [18, 20])
def test_use_param(name,age):
    assert name == "Mark" and age == 20


"""
F:\自动化测试\08-pytest\02-pytest编写测试用例\参数化测试>pytest test02_param.py
======================================== test session starts =========================================
platform win32 -- Python 3.8.3, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: F:\自动化测试\08-pytest\02-pytest编写测试用例\参数化测试
plugins: allure-pytest-2.9.45
collected 4 items                                                                                     

test02_param.py FF.F                                                                            [100%]

============================================== FAILURES ==============================================
______________________________________ test_use_param[18-Mark] _______________________________________

name = 'Mark', age = 18

    @pytest.mark.parametrize("name", ["Mark", "Joe"])
    @pytest.mark.parametrize("age", [18, 20])
    def test_use_param(name,age):
>       assert name == "Mark" and age == 20
E       AssertionError: assert ('Mark' == 'Mark'
E           Mark and 18 == 20)

test02_param.py:11: AssertionError
_______________________________________ test_use_param[18-Joe] _______________________________________

name = 'Joe', age = 18

    @pytest.mark.parametrize("name", ["Mark", "Joe"])
    @pytest.mark.parametrize("age", [18, 20])
    def test_use_param(name,age):
>       assert name == "Mark" and age == 20
E       AssertionError: assert ('Joe' == 'Mark'
E         - Mark
E         + Joe)

test02_param.py:11: AssertionError
_______________________________________ test_use_param[20-Joe] _______________________________________

name = 'Joe', age = 20

    @pytest.mark.parametrize("name", ["Mark", "Joe"])
    @pytest.mark.parametrize("age", [18, 20])
    def test_use_param(name,age):
>       assert name == "Mark" and age == 20
E       AssertionError: assert ('Joe' == 'Mark'
E         - Mark
E         + Joe)

test02_param.py:11: AssertionError
====================================== short test summary info =======================================
FAILED test02_param.py::test_use_param[18-Mark] - AssertionError: assert ('Mark' == 'Mark'
FAILED test02_param.py::test_use_param[18-Joe] - AssertionError: assert ('Joe' == 'Mark'
FAILED test02_param.py::test_use_param[20-Joe] - AssertionError: assert ('Joe' == 'Mark'
==================================== 3 failed, 1 passed in 0.09s =====================================

"""

