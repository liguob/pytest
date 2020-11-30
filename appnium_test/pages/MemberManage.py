# -*- coding: utf-8 -*-
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appnium_test.pages.AddContactPage import AddContactPage
from appnium_test.pages.BasePage import BasePage
from appnium_test.pages.MemberInvitePage import MemberInvitePage


class MemberManage(BasePage):
    _members = '//android.widget.ListView//android.widget.TextView'
    _addmember = '//android.widget.TextView[@text="手动输入添加"]'

    def goto_addcontact(self):
        self.scoll_to_element('添加成员').click()
        self.find(MobileBy.XPATH, self._addmember).click()
        return AddContactPage(self.driver)

    def goto_memberinvite(self, name):
        self.scoll_to_element(name).click()
        return MemberInvitePage(self.driver)

    def get_member(self):
        sleep(1)
        return [i.text for i in self.finds(MobileBy.XPATH, self._members)]
