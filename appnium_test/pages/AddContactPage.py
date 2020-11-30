# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from appnium_test.pages.BasePage import BasePage


class AddContactPage(BasePage):
    _name_xpath = '//*[contains(@text,"姓名")]/../*[@text="必填"]'
    _phonenum_xpath = '//*[@text="手机号"]'
    _gender_xpath1 = '//*[@text="男"]'
    _gender_xpath2 = '//*[@text="女"]'
    _save_path = '//*[@text="保存"]'

    def edit_name(self, name):
        self.find(MobileBy.XPATH, self._name_xpath).send_keys(name)
        return self

    def edit_phone(self, phonenum):
        self.find(MobileBy.XPATH, self._phonenum_xpath).send_keys(phonenum)
        return self

    def edit_gender(self, gender):
        # _gender_xpath2 = '//[text()={}]'.format(gender)
        # self.find(MobileBy.XPATH, self._gender_xpath1).click()
        # self.find(MobileBy.XPATH, self._gender_xpath2).click()
        if gender == '男':
            return self
        else:
            self.find(MobileBy.XPATH, self._gender_xpath1).click()
            self.find(MobileBy.XPATH, self._gender_xpath2).click()
            return self

    def save_member(self):
        self.find(MobileBy.XPATH, self._save_path).click()
        self.back()
        from appnium_test.pages.MemberManage import MemberManage
        return MemberManage(self.driver)
