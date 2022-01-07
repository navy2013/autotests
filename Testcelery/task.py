#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/24 21:00

from celery import Celery

app = Celery('task',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/1'
             )


@app.task
def add(x,y):
    print("running...",x,y)
    return x+y



