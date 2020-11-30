# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from appnium_test.pages.BasePage import BasePage
from appnium_test.pages.MemberManage import MemberManage


class HomePage(BasePage):

    def goto_membermanage(self):
        xpath1 = '//android.widget.TextView[@text="通讯录"]'
        self.find(MobileBy.XPATH, xpath1).click()
        return MemberManage(self.driver)