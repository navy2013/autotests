#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 9:43

import yaml
aproject = {'name':'Silenthand Olleander',
            'race':'Human',
            'traits':['ONE_HAND','ONE_EYE']}
f = open('./test_yaml_dump.yml','w')
f.write(yaml.dump(aproject,))
f.close()

# print(yaml.dump(aproject,))
# name: Silenthand Olleander
# race: Human
# traits:
# - ONE_HAND
# - ONE_EYE


