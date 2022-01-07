#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/20 21:44

import pytest
from python.calc import Calc

class TestCal():

    @pytest.fixture()
    def yc_self(self):
        self.calc = Calc()

    @pytest.mark.parametrize('a,b,c',[(0,0,0),(1,2,3),(3,4,7)])
    def test_add(self,yc_self,a,b,c):
        result = self.calc.add(a,b)
        assert result == c

    @pytest.mark.parametrize('a,b,c', [(0, 0, 0), (1, 2, -1), (3, 4, -1)])
    def test_sub(self,yc_self, a, b, c):
        result = self.calc.sub(a, b)
        assert result == c

    @pytest.mark.parametrize('a,b,c', [(0, 0, 0), (1, 2, 2), (3, 4, 12)])
    def test_mul(self,yc_self, a, b, c):
        result = self.calc.mul(a, b)
        assert result == c

    @pytest.mark.parametrize('a,b,c', [(0, 0, 0), (1, 2, 3), (3, 4, 5)])
    def test_div(self, yc_self,a, b, c):
        result = self.calc.div(a, b)
        assert result == c




