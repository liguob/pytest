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
        # if gender == '男':
        #     return self
        # 本地模拟器上微信的bug，使用默认性别，保存按钮置灰无法点击，选择性别后可点击
        if gender == '男':
            self.find(MobileBy.XPATH, self._gender_xpath1).click()
            #如果选择为男性时，不进行显示等待，会找不到元素
            self.display_wait((MobileBy.XPATH, self._gender_xpath1))
            self.find(MobileBy.XPATH, self._gender_xpath1).click()
        else:
            self.find(MobileBy.XPATH, self._gender_xpath1).click()
            self.find(MobileBy.XPATH, self._gender_xpath2).click()
        return self

    def save_member(self):
        self.find(MobileBy.XPATH, self._save_path).click()
        self.back()
        from appnium_test.pages.MemberManage import MemberManage
        return MemberManage(self.driver)
