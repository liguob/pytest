import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver

    def find(self, *locator, time=3):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(*locator))

    def finds(self, *locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_all_elements_located(*locator))

    def input_text_value(self, by: By, element, value):
        self.driver.find_element(by, element).send_keys(value)
