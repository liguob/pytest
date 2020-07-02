from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        """
        若driver为None,则初始化driver
        :param driver: Chrome的driver
        """
        option = Options()
        option.debugger_address = 'localhost:9999'
        # 调用构造函数时，若传入的driver非空，则使用传入参数，为空则初始化
        if driver is None:
            self.driver = webdriver.Chrome(options=option)
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def display_wait(self, *locator, time=30):
        """
        封装显示等待,若没有找到元素则打印信息
        :param locator: 定位元素元祖
        :param time: 默认时长30秒
        """
        result = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(*locator))
        if result is None:
            print("element can't be located")

    def find(self, by: By, element):
        """
        :param by: 定位元素方法
        :param element: 元素路径
        :return: 返回定位结果
        """
        return self.driver.find_element(by, element)
    
    def finds(self, by: By, element):
        """
        :param by: 定位元素方法
        :param element: 元素路径
        :return: 返回定位结果
        """
        return self.driver.find_elements(by, element)
