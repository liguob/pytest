from selenium.webdriver.common.by import By

from selenium_test.pages.addmemberpage import AddMemberPage
from selenium_test.pages.basepage import BasePage
from selenium_test.pages.contactmemberpage import ContactMemberPage
from selenium_test.pages.importpage import ImportPage


class HomePage(BasePage):

    def goto_add_contact(self):
        """
        进入添加联系人界面
        :return: 返回添加联系人page
        """
        self.driver.find_element(By.XPATH, "//span[text()='添加成员']").click()
        return AddMemberPage(self.driver)

    def goto_upload(self):
        """
        进入通讯录上传界面
        :return: 返回通讯录上传page
        """
        self.driver.find_element(By.XPATH, "//span[text()='导入通讯录']").click()
        return ImportPage(self.driver)

    def goto_members(self):
        """
        进入通讯录界面
        :return: 返回通讯录page
        """
        self.driver.find_element(By.CSS_SELECTOR, '#menu_contacts').click()
        return ContactMemberPage(self.driver)