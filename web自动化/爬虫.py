# ！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/28 21:43

import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.baidu.com')
res.encoding='utf8'
print(res.text)
soup = BeautifulSoup(res.text, 'lxml')

print(soup.a)



