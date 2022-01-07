#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/19 21:08
import unittest

from python.calc import Calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(1,2)
        print(result)
        self.assertEqual(3,result)





