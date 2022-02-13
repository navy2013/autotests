#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/2/13 12:01
import pytest


def add(x, y):
    return x + y


def test_add_1():
    assert add(1, 2) == 3

@pytest.mark.demo01
def test_add_2():
    assert add(2, 2) == 3



