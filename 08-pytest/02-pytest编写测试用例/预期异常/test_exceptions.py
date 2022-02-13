#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/2/13 15:15

import pytest


# def test_add_raises():
#     '''测试一个肯定会报ValueError异常的用例'''
#     str_to_change = '非数字字符不能转数字'
#     num = int(str_to_change)


"""
F:\自动化测试\08-pytest\02-pytest编写测试用例\预期异常>pytest
======================================== test session starts =========================================
platform win32 -- Python 3.8.3, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: F:\自动化测试\08-pytest\02-pytest编写测试用例\预期异常
plugins: allure-pytest-2.9.45
collected 1 item                                                                                      

test_exceptions.py F                                                                            [100%]

============================================== FAILURES ==============================================
__________________________________________ test_add_raises ___________________________________________

    def test_add_raises():
        '''测试一个肯定会报ValueError异常的用例'''
        str_to_change = '非数字字符不能转数字'
>       num = int(str_to_change)
E       ValueError: invalid literal for int() with base 10: '非数字字符不能转数字'

test_exceptions.py:12: ValueError
====================================== short test summary info =======================================
FAILED test_exceptions.py::test_add_raises - ValueError: invalid literal for int() with base 10: '非...
========================================= 1 failed in 0.08s ==========================================

"""




def test_add_raises():
    '''测试一个肯定会报ValueError异常的用例'''
    str_to_change = '非数字字符不能转数字'
    with pytest.raises(ValueError):  # 预期下面的代码会抛ValueError
        num = int(str_to_change)

"""
F:\自动化测试\08-pytest\02-pytest编写测试用例\预期异常>pytest
=============================================================================== test session starts ===============================================================================
platform win32 -- Python 3.8.3, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: F:\自动化测试\08-pytest\02-pytest编写测试用例\预期异常
plugins: allure-pytest-2.9.45
collected 1 item                                                                                                                                                                   

test_exceptions.py .                                                                                                                                                         [100%]

================================================================================ 1 passed in 0.02s ================================================================================

"""