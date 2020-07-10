# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from appnium_test.pages.BasePage import BasePage


class DelContactPage(BasePage):
    _edit = '//*[@text="编辑成员"]'
    _del = '//*[@text="删除成员"]'
    _confirm = '//*[@text="确定"]'
    _cancle = '//*[@text="取消"]'

    def del_confirm(self):
        self.find(MobileBy.XPATH, self._edit).click()
        self.find(MobileBy.XPATH, self._del).click()
        self.find(MobileBy.XPATH, self._confirm).click()
        from appnium_test.pages.MemberManage import MemberManage
        return MemberManage(self.driver)

    def cancle(self):
        self.find(MobileBy.XPATH, self._edit).click()
        self.find(MobileBy.XPATH, self._del).click()
        self.find(MobileBy.XPATH, self._cancle).click()
        return self