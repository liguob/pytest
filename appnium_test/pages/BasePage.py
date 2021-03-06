# -*- coding: utf-8 -*-
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def scoll_to_element(self, text):
        return self.driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));')

    def find(self, by: MobileBy, xpath):
        return self.driver.find_element(by, xpath)

    def finds(self, by: MobileBy, xpath):
        return self.driver.find_elements(by, xpath)

    def toast_text(self, text):
        _text_message = f'//*[@text="{text}"]'
        return self.find(MobileBy.XPATH, _text_message).text

    def back(self, time: int = 1):
        for i in range(time):
            self.driver.back()

    def display_wait(self, locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
