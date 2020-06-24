from selenium.webdriver.common.by import By

from selenium_test.pages.addmemberpage import AddMemberPage
from selenium_test.pages.basepage import BasePage
from selenium_test.pages.importpage import ImportPage


class HomePage(BasePage):

    def goto_add_contact(self):
        self.find((By.CSS_SELECTOR, '.ww_indexImg ww_indexImg_AddMember')).click()
        return AddMemberPage(self.driver)

    def goto_upload(self):
        self.find((By.CSS_SELECTOR, '.ww_indexImg ww_indexImg_Import')).click()
        return ImportPage(self.driver)