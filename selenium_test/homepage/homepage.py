from selenium.webdriver.common.by import By

from selenium_test.basepage.basepage import BasePage
from selenium_test.contactmember.contactmemberpage import ContactMemberPage
from selenium_test.importpage.importpage import ImportPage


class HomePage(BasePage):

    def goto_add_contact(self):
        self.find((By.CSS_SELECTOR, '.ww_indexImg ww_indexImg_AddMember')).click()
        return ContactMemberPage(self.driver)

    def goto_upload(self):
        self.find((By.CSS_SELECTOR, '.ww_indexImg ww_indexImg_Import')).click()
        return ImportPage(self.driver)
