#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/11/30 22:11
import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()


    def test_demo(self):
        # self.driver.get('https://ceshiren.com/')
        # self.driver.find_element(By.XPATH,'//*[@id="ember45"]/a').click()
        #cookies = [{'domain': '.ceshiren.com', 'httpOnly': False, 'name': 'Hm_lpvt_214f62eef822bde113f63fedcab70931', 'path': '/', 'secure': False, 'value': '1638282682'}, {'domain': 'ceshiren.com', 'expiry': 1643466225, 'httpOnly': True, 'name': '_t', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'OVJTSWlpdlByeDBaL3ZGMmtDTXRMeVYvY2VQK0NWWFFrWm56NmJIVU1TbmxSdTlrVHJzYVphaEtkd0xZWStBSXg5MytEYWVBVkNjZHRhcVkyTHpGK2NsRWVJc21nd3RpZmttNklvQzBhdFdIRFVzVm9sRlN6c2hpdk5OT1BzQkw1NlJzS0l0S0tEQmFNeWJxRTJQa2VIeDFyMEQyWUpEczNQOG9NR1pVTUppaFVuVURxQ1ZDem5EcXUwbWdOM0ZITWRCSi9SdVhIYklZRFRiNStMbkpsVmhLYkpKVThQcHBBa29aYTVZZ0hJcFg3ZE1ndkhEVjJ1TjVuNEZCaGo4UkxhQXFnUUtKS3hYU2k3MXJqV3c4VWc9PS0tQTBNblF0dmNKZVBhQjBnS3h5NnJFQT09--3d4627016bb71cf803b620e1caf03da487ba5bd7'}, {'domain': '.ceshiren.com', 'expiry': 1638369082, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.832578027.1638276730'}, {'domain': '.ceshiren.com', 'expiry': 1638282742, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.ceshiren.com', 'expiry': 1669818682, 'httpOnly': False, 'name': 'Hm_lvt_214f62eef822bde113f63fedcab70931', 'path': '/', 'secure': False, 'value': '1638276730,1638276745,1638282198,1638282682'}, {'domain': 'ceshiren.com', 'httpOnly': True, 'name': '_forum_session', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'UmlRRjBYM0NFdi9QYitxZWdYNGpvVFVPckdiS3BuY0NVM1BjV1hhQ1p1K1BXbnE2REd4cXloc3U2bncyWXhka0JkVEpaMmFOUlJrdmtVV0JPL3NGNXNoMll5bXBzSUk3RXBZOThuZ3haN3FFU1B2c01hTW9KQ2RSUSt5TG1GdFFIVDVtdUZWdkdUbHlCb3Fab2cyRk5jUFYzZlVobjZLMXpnSUlWU1VoVjJNd29ib3dHcHFIT0l6WFN6eVZPUmJhLS1rUDVwUml4c3NVeTZMak15VERBMUxRPT0%3D--90609542a85bc9e0ddaa7d798ee1f0c6d283c533'}, {'domain': '.ceshiren.com', 'expiry': 1701354682, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.723726488.1634960199'}]
        db = shelve.open("cookies")
        db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        self.driver.get('https://ceshiren.com/')
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://ceshiren.com/')
        time.sleep(8)
        db.close()


