# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/22 15:56
@Author  : liguobin
@File    : contactmember.py
"""
from selenium.webdriver.common.by import By

from selenium_test.basepage.basepage import BasePage
from selenium_test.homepage.homepage import HomePage


class ContactMemberPage(BasePage):

    def add_member(self):
        self.input_text_value(By.CSS_SELECTOR, '#username', 'test1')
        self.input_text_value(By.CSS_SELECTOR, '#memberAdd_acctid','测试账号1')
        self.input_text_value(By.CSS_SELECTOR, '#memberAdd_phone','13199991001')
        element = self.finds(By.CSS_SELECTOR, '.js_btn_save','13199991001')
        element[0].click()

    def delete_member(self):
        pass

