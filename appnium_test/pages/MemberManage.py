# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from appnium_test.pages.AddContactPage import AddContactPage
from appnium_test.pages.BasePage import BasePage
from appnium_test.pages.MemberInvitePage import MemberInvitePage


class MemberManage(BasePage):
    _members = '//*[@class="android.widget.ListView"]//*[@class="android.widget.TextView"]'

    def goto_addcontact(self):
        self.scoll_to_element('添加成员').click()
        return AddContactPage(self.driver)

    def goto_memberinvite(self, name):
        self.scoll_to_element(name).click()
        return MemberInvitePage(self.driver)

    def get_member(self, name):
        self.display_wait((MobileBy.XPATH, '//*[@text="{}"]'.format(name)))
        return [i.text for i in self.finds(MobileBy.XPATH, self._members)]