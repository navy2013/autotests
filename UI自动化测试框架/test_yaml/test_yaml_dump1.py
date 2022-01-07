#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 9:50

import yaml
aproject = {'name1': 'Silenthand Olleander',
            'race': 'Human',
            'traits': ['ONE_HAND', 'ONE_EYE']
            }

f = open('./config.yml','a')
yaml.dump(aproject,f)



