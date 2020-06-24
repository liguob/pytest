from selenium.webdriver.common.by import By

from selenium_test.pages.basepage import BasePage


class ContactMemberPage(BasePage):

    def get_members(self):
        members = self.find(By.CSS_SELECTOR, '#member_list td:nth-child(2)').text
        return members

    def add_member(self, name: str, acctid: str, phone: int):
        self.input_text_value(By.CSS_SELECTOR, '#username', name)
        self.input_text_value(By.CSS_SELECTOR, '#memberAdd_acctid', acctid)
        self.input_text_value(By.CSS_SELECTOR, '#memberAdd_phone', phone)
        element = self.finds(By.CSS_SELECTOR, '.js_btn_save')
        element[0].click()
        return ContactMemberPage(self.driver)

    def delete_member(self, name: str):
        self.find(By.XPATH, '//td[@title={}]/parent::tr/td[1]/input'.format(name))
        self.finds(By.CSS_SELECTOR, '.js_delete')[0].click()
        self.find(By.CSS_SELECTOR, '[d_ck=submit]').click()
        return ContactMemberPage(self.driver)
