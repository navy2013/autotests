#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/6 0:37

# import yaml
#
# f = open(r'F:\软件测试\b\config.yml')
# y = yaml.load(f,Loader=yaml.FullLoader)
#
# print(y)


# import yaml
# f = open('config_all.yml')
# y = yaml.load_all(f,Loader=yaml.FullLoader)
# for data in y:
#     print(data)

# import yaml
#
# aproject = {'name':'Silenthand Olleander',
#             'race':'Human',
#             'traits':['ONE_HAND','ONE_EYE']
#             }
#
# f = open('config_dump.yml','w')
#
# yaml.dump(aproject,f)
# print(yaml.load(open('config_dump.yml')))


import yaml

obj1 = {"name":"James","age":20}
obj2 = ["Lily",19]


with open('config.yml','w') as f:
    yaml.dump_all([obj1,obj2],f)