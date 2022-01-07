#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 9:58

import yaml
class Person(yaml.YAMLObject):
    yaml_tag = "!person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '%s(name=%s, age=%d)' %(self.__class__.__name__, self.name, self.age)

james = Person('James', 20)
print(yaml.dump(james))
lily = yaml.load('!person {name:Lily,age:19}')
print(lily)


