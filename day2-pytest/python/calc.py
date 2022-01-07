# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/19 21:06

class Calc:

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        try:
            return a / b
        except Exception as e:
            return "除数不能为0"

    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        return a * b
