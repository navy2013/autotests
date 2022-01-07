#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/19 22:11

import pytest
from python.calc import Calc


class TestCalc:
    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(1,2)
        print(result)
        assert 3 == result

    def test_div(self):
        self.calc = Calc()
        result = self.calc.div(1,1)
        print(result)
        assert 1 == result

if __name__ == '__main__':
    pytest.main(['-vs','test_pytest.py::TestCalc::test_div'])