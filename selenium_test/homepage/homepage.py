# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/22 16:01
@Author  : liguobin
@File    : indexpage.py
"""
from selenium.webdriver.common.by import By

from selenium_test.basepage.basepage import BasePage


class HomePage(BasePage):

    def goto_contact(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_item_title')
        return self.driver

    def goto_upload(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_item_title')
        return self.driver