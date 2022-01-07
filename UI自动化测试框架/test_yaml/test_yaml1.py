#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 9:39

import yaml
f = """
---
name: James
age: 20
---
name: Lily
age: 19
"""
y = yaml.load_all(f) # 生成一个迭代器
for data in y:
    print(data)
# {'name': 'James', 'age': 20}
# {'name': 'Lily', 'age': 19}


