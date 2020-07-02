from time import sleep

from selenium.webdriver.common.by import By

from selenium_test.pages.basepage import BasePage
from selenium_test.pages.contactmemberpage import ContactMemberPage


class ImportPage(BasePage):

    def upload_file(self,file):
        """
        上传文件并返回到联系人界面
        :param file: 文件路径
        :return: 联系人界面
        """
        self.find(By.CSS_SELECTOR, '#js_upload_file_input').send_keys(file)
        self.find(By.CSS_SELECTOR, '#submit_csv').click()
        self.find(By.CSS_SELECTOR, '#reloadContact').click()
        return ContactMemberPage(self.driver)
