#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/2/13 15:07

import pytest

version = 5


def add(x, y):
    return x + y


def test_add_1():
    assert add(1, 2) == 3


@pytest.mark.skip(reason="这里是跳过的原因")
def test_add_2():
    assert add(2, 2) == 3


@pytest.mark.skipif(version == 5, reason="如果版本号等于5就跳过")
def test_add_3():
    assert add(2, 2) == 3


