from selenium.webdriver.common.by import By

from selenium_test.pages.basepage import BasePage
from selenium_test.pages.contactmemberpage import ContactMemberPage


class AddMemberPage(BasePage):
    def add_member(self, name: str, acct_id: str, phone: int):
        self.input_text_value(By.CSS_SELECTOR, '#username', name)
        self.input_text_value(By.CSS_SELECTOR, '#memberAdd_acctid', acct_id)
        self.input_text_value(By.CSS_SELECTOR, '#memberAdd_phone', phone)
        element = self.finds(By.CSS_SELECTOR, '.js_btn_save')
        element[0].click()
        return ContactMemberPage(self.driver)