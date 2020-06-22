# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/22 17:07
@Author  : liguobin
@File    : basemethod.py
"""
import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    _address = 'localhost:9999'
    _option = Options()
    _option.debugger_address = _address
    driver = webdriver.Chrome(options=_option)
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    driver.implicitly_wait(3)

    def find(self, element):
        return self.driver.find_element(By.ID, element)

    def login(self):
        # 登陆企业微信
        _id = 'menu_index'
        file_exist = os.path.exists(self.cookie_file)
        # 判断cookies文件是否存在，存在则读取,不存在则保存cookis
        if file_exist:
            with open(self.cookie_file, 'r') as f:
                self.cookies = json.load(f)
                for cookie in self.cookies:
                    self.driver.add_cookie(cookie)
                while True:
                    self.driver.refresh()
                    result = WebDriverWait(self.driver, 30).until(self.find(By.ID, _id))
                    if result is not None:
                        return True
                        break
                return False
        else:
            self.is_login('menu_index', time=20)
            self.cookies = self.driver.get_cookies()
            with open(self.cookie_file, 'w') as f:
                json.dump(self.cookies, f)
