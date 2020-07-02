from selenium.webdriver.common.by import By

from selenium_test.pages.basepage import BasePage
from selenium_test.pages.contactmemberpage import ContactMemberPage


class AddMemberPage(BasePage):
    def add_member(self, name: str, acct_id: str, phone: int):
        """
        通讯录界面添加人员
        :param name: 添加人员名称
        :param acct_id: 添加人员id
        :param phone: 添加人员电话
        :return: 返回通讯录
        """
        self.find(By.CSS_SELECTOR, '#username').send_keys(name)
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(acct_id)
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(phone)
        self.finds(By.CSS_SELECTOR, '.js_btn_save')[0].click()
        return ContactMemberPage(self._driver)