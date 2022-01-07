#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/19 23:32

import selenium
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("http:www.baidu.com")
    driver.close()