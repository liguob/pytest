# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from appnium_test.pages.BasePage import BasePage
from appnium_test.pages.HomePage import HomePage


class App(BasePage):

    def start(self, driver: WebDriver = None):
        if driver is None:
            _caps = {}
            _caps['deviceName'] = '127.0.0.1:7555'
            _caps['platformName'] = 'Android'
            _caps['appActivity'] = '.launch.WwMainActivity'
            _caps['appPackage'] = 'com.tencent.wework'
            _caps['noReset'] = True
            _caps['automationName'] = 'UiAutomator2'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', _caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver
        return self

    def lauch_app(self):
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def main(self):
        return HomePage(self.driver)