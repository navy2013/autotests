#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/17 23:31

def provide():
    for i in range(5):
        print("before")
        yield i
        print("after")


p = provide()
print(next(p))
print(next(p))
# print(next(p))


