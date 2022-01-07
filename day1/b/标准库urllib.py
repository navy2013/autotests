#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/1 23:28

import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response.status)
print(response.read())

import math

print(math.ceil(5.5))   # 6
print(math.floor(5.9))  # 5
print(math.sqrt(4))


