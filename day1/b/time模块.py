#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/9/29 20:55

import time

print(time.time())  # 1632920259.9138563
print(time.asctime()) # Wed Sep 29 20:57:39 2021

print(time.localtime()) # time.struct_time(tm_year=2021, tm_mon=9, tm_mday=29, tm_hour=20, tm_min=58, tm_sec=10, tm_wday=2, tm_yday=272, tm_isdst=0)

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))


