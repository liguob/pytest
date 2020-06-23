import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium_test.basepage.basepage import BasePage


class LoginPage(BasePage):
    def login(self):
        # 登陆企业微信
        _id = 'menu_index'
        _cookie_file = './cookie.json'
        file_exist = os.path.exists(_cookie_file)
        # 判断cookies文件是否存在，存在则读取,不存在则保存cookis
        if file_exist:
            with open(_cookie_file, 'r') as f:
                _cookies = json.load(f)
                for cookie in _cookies:
                    self.driver.add_cookie(cookie)
                while True:
                    self.driver.refresh()
                    result = WebDriverWait(self.driver, 20).until(self.find(By.ID, _id))
                    if result is not None:
                        break
        else:
            self.find(By.ID, _id)
            _cookies = self.driver.get_cookies()
            with open(_cookie_file, 'w') as f:
                json.dump(_cookies, f)
