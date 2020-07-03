# -*- coding: utf-8 -*-

from appium import webdriver


class BasePage:
        caps = {}
        caps['deviceName'] = '127.0.0.1:7555'
        caps['platformName'] = 'Android'
        caps['appActivity'] = '.launch.WwMainActivity'
        caps['appPackage'] = 'com.tencent.wework'
        caps['noReset'] = True

        driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        driver.implicitly_wait(5)
        driver.quit()


if __name__ == '__main__':
    test = BasePage()