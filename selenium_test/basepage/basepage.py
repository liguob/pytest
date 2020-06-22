# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/22 17:07
@Author  : liguobin
@File    : basepage.py
"""
import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def setup(self):
        _address = 'localhost:9999'
        _option = Options()
        _option.debugger_address = _address
        if self.driver is not None:
            self.driver = webdriver.Chrome(options=_option)
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
            self.implicitly_wait(3)

    def find(self, by: By, element):
        return self.driver.find_element(by, element)

    def finds(self, by: By, element):
        return self.driver.find_elements(by, element)

    def input_text_value(self, by: By, element, value):
        self.driver.find_element(by, element).send_keys(value)

    def display_wait(self, by: By,element, time):
        while True:
            result = WebDriverWait(self.driver, time).until(self.find(by, element))
            if result is not None:
                break

    def login(self):
        # 登陆企业微信
        _id = 'menu_index'
        _cookie_file = './cookie.json'
        file_exist = os.path.exists(self._cookie_file)
        # 判断cookies文件是否存在，存在则读取,不存在则保存cookis
        if file_exist:
            with open(self._cookie_file, 'r') as f:
                self.cookies = json.load(f)
                for cookie in self.cookies:
                    self.driver.add_cookie(cookie)
                while True:
                    self.driver.refresh()
                    result = WebDriverWait(self.driver, 20).until(self.find(By.ID, self._id))
                    if result is not None:
                        break
        else:
            self.display_wait(By.ID, 'menu_index')
            self._cookies = self.driver.get_cookies()
            with open(self._cookie_file, 'w') as f:
                json.dump(self.cookies, f)
