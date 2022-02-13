#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/2/13 12:00
import pytest


@pytest.mark.demo01
def test_passing():
    assert (1, 2, 3) == (1, 2, 3)



