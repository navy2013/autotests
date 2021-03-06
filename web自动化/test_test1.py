# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_test1(self):
    self.driver.get("https://www.baidu.com/")
    self.driver.set_window_size(1285, 1112)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "NBA官宣！鹈鹕后卫被禁赛25场！赛季场均0分1篮板").click()
    self.vars["win5519"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win5519"])
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "消失56天！八村塁首次被媒体拍到！库兹马已经抢走他的首发").click()
    self.vars["win7242"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win7242"])
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "10分9篮板2盖帽！周琦在季前赛被绝杀！他即将和中国男篮汇合").click()
    self.vars["win701"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win701"])
  
