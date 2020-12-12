# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from appnium_test.pages.BasePage import BasePage
from appnium_test.pages.DelContactPage import DelContactPage


class MemberInvitePage(BasePage):

    def goto_delcontact(self, name: str):
        _xpath = '//android.widget.RelativeLayout/android.widget.TextView[@text=""]'
        self.scoll_to_element(name).click()
        self.find(MobileBy.XPATH, _xpath).click()
        return DelContactPage(self.driver)