#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 9:55

import yaml
obj1 = {'name2':"James","age":20}
obj2 = ["lily",19]

with open('./config.yml','a') as f:
    yaml.dump_all([obj1,obj2],f)


