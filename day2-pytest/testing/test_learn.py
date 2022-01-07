#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/20 22:23


import pytest


# fixtrue作为参数，互相调用传入
@pytest.fixture()
def account():
    a = "account"
    print("第一层fixture")
    return a


# Fixture的相互调用一定是要在测试类里调用这层fixture才会生次，普通函数单独调用是不生效的
@pytest.fixture()
def login(account):
    print("第二层fixture")


def test_3(login):
    print("直接使用fixture,返回值为{}".format(login))

class TestLogin:
    def test_1(self, login):
        print("直接使用第二层fixture,返回值为{}".format(login))

    def test_2(self, account):
        print("只调用account fixture,返回值为{}".format(account))


if __name__ == '__main__':
    pytest.main()



