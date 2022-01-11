#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/11 15:04

import logging

datefmt = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(filename)s:%(message)s", datefmt=datefmt, filename="test.log", filemode="a+")

logging.info("hello world!")


