#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/7 23:15

import pytest

def setup_module():
    print("这是个setup_module方法")

def teardown_module():
    print("这是个teardown_module方法")

def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def test_login():
    print("这是一个外部方法")

class testDemo():
    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def setup(self):
        print("setup")

    def teardown_class(self):
        print("teardown_class")


    def teardown_method(self):
        print("teardown_method")

    def teardown(self):
        print("teardown")

    def test_one(self):
        print("开始执行testone方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行testtwo方法")
        x = 'hello'
        assert 'e' in x

if __name__ == '__main__':
    pytest.main()


