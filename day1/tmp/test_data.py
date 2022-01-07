#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/18 20:23
import pytest
import yaml

class TestData:
    # @pytest.mark.parametrize(['a','b'],[(10,20),(11,20),(12,20)])
    # def test_data(self,a,b):
    #     print(a+b)

    @pytest.mark.parametrize('a,b', yaml.safe_load(open('./data.yaml')))
    def test_data(self, a, b):
        print(a + b)



