# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/22 15:56
@Author  : liguobin
@File    : contactmemberpage.py
"""
from selenium.webdriver.common.by import By
from selenium_test.basepage.basepage import BasePag


class ContactMemberPage:

    def add_member(self, name: str, acctid: str, phone: int):
        self.input_text_value(By.CSS_SELECTOR, '#username', name)
        self.input_text_value(By.CSS_SELECTOR, '#memberAdd_acctid', acctid)
        self.input_text_value(By.CSS_SELECTOR, '#memberAdd_phone', phone)
        element = self.finds(By.CSS_SELECTOR, '.js_btn_save')
        element[0].click()
        members = self.find(By.CSS_SELECTOR, '#member_list td:nth-child(2)').text
        if name in members:
            return True
        else:
            return False

    def delete_member(self, name: str):
        self.find(By.XPATH, '//td[@title={}]/parent::tr/td[1]/input'.format(name))
        self.finds(By.CSS_SELECTOR, '.js_delete')[0].click()
        self.find(By.CSS_SELECTOR, '[d_ck=submit]').click()
        members = self.find(By.CSS_SELECTOR, '#member_list td:nth-child(2)').text
        if name not in members:
            return True
        else:
            return False
