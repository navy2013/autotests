#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/7 22:12
import pytest

def test_a():
    print("执行test_a")

class TestDemo():
    def test_one(self):
        print("开始执行 test_one方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行 test_two方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three方法")
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
    # pytest.main("-v -x TestDemo")
    # pytest.main(["-v", "-x", "TestDemo"])
    pytest.main()