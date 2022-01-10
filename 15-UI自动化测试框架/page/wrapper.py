#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/10 15:36
import logging

from selenium.webdriver.common.by import By




def hander_black(func):
    def wrapper(*args, **kwargs):
        from page.base_page import BasePage
        logging.basicConfig(level=logging.INFO)
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]
        _max_num = 3
        _error_num = 0
        instance: BasePage = args[0]
        try:
            element = func(*args, **kwargs)
            # 找到之后 _error_num 归0
            _error_num = 0
            # 隐式等待恢复原来的等待
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
        # 出现异常，将隐式等待设置小一点，快速的处理弹框
            instance._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                logging.info(ele)
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper
