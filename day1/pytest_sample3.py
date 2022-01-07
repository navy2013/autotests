#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/7 23:35

import pytest

@pytest.fixture()
def login():
    print("这是个登录方法")

def test_case1(login):
    print("test_case1,要登陆")
    pass

def test_case2():
    print("test_case2,不要登陆")
    pass

def test_case3(login):
    print("test_case3,要登陆")
    pass

if __name__ == '__main__':
    pytest.main()

