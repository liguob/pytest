import json
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait


class TestSelenium():
    def setup(self):
        self.cookie_file = 'cookies.json'
        self.option = Options()
        self.option.debugger_address = 'localhost:9999'
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.maximize_window()

    def is_login(self, id, time=10):
        while True:
            self.driver.refresh()
            sleep(1)
            result = WebDriverWait(self.driver, time).until(ES.presence_of_element_located((By.ID, 'menu_index')))
            if result is not None:
                break

    def test_login(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        file_exist = os.path.exists(self.cookie_file)
        # 判断cookies文件是否存在，存在则读取,不存在则保存cookis
        if file_exist:
            file_size = os.path.getsize(self.cookie_file)
            with open(self.cookie_file, 'r') as f:
                self.cookies = json.load(f)
                for cookie in self.cookies:
                    self.driver.add_cookie(cookie)
                self.is_login('menu_index')
        else:
            self.is_login('menu_index', time=20)
            self.cookies = self.driver.get_cookies()
            with open(self.cookie_file, 'w') as f:
                json.dump(self.cookies, f)
            print(self.cookies)

    def test_uploadfile(self):
        # 导入通讯录
        self.driver.find_element(By.XPATH, "//span[text()='导入通讯录']").click()
        WebDriverWait(self.driver, 5).until(ES.presence_of_element_located((By.ID, 'js_upload_file_input')))
        self.driver.find_element(By.ID, 'js_upload_file_input').send_keys('D:\\用户目录\\下载\\通讯录批量导入模板.xlsx')
        WebDriverWait(self.driver, 5).until(ES.presence_of_element_located((By.ID, 'upload_file_name')))
        assert self.driver.find_element(By.ID, 'upload_file_name').text == '通讯录批量导入模板.xlsx'

    def teardown(self):
        self.driver.quit()
