from time import sleep

from selenium.webdriver.common.by import By
from selenium_test.pages.basepage import BasePage


class ContactMemberPage(BasePage):

    def get_members(self):
        """
        获取通讯录中已有的人员名称
        :return: 返回的人员名称列表
        """
        members = self.driver.find_elements(By.CSS_SELECTOR, '.js_ww_table td:nth-child(2)')
        member_list = [i.text for i in members]
        return member_list

    def add_member(self, name: str, acct_id: str, phone: int):
        """
        :param name: 界面输入的成员名称
        :param acct_id: 输入的acct_id
        :param phone: 输入的电话号码
        :return: 返回通讯录
        """
        self.find(())
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(acct_id)
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(phone)
        self.driver.find_elements(By.CSS_SELECTOR, '.js_btn_save')[0].click()
        return ContactMemberPage(self.driver)

    def delete_member(self, name: str):
        """
        删除指定的人员
        :param name: 删除人员的名称
        :return: 返回通讯录
        """
        self.driver.find_element(By.XPATH, "//td[@title='{}']/../td[1]".format(name)).click()
        self.driver.find_elements(By.CSS_SELECTOR, '.js_delete')[0].click()
        self.driver.find_element(By.CSS_SELECTOR, '[d_ck=submit]').click()
        sleep(3)
        return ContactMemberPage(self.driver)