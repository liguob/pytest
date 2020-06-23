import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_test.indexpage.Loginpage import LoginPage


@pytest.fixture(scope='class')
def setup():
    option = Options()
    driver = webdriver.Chrome(option)
    option.debugger_address = 'localhost:9999'
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    stat = LoginPage()
    stat.driver = driver
    stat.login()