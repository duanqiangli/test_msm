"""定义基类"""
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        """
        初始化手机驱动对象
        :param driver: 传入driver
        """
        self.driver = driver
        ...

    def get_element(self, loc, timeout=30, poll_frequency=1.0):
        """
        查找单个元素
        :param loc: 元素定位方法
        :param timeout: 等待时间
        :param poll_frequency: 间隔时长
        :return: 单个元素
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=30, poll_frequency=1.0):
        """
        查找多个元素
        :param loc: 元素定位方法
        :param timeout: 等待时间
        :param poll_frequency: 间隔时长
        :return: 多个元素
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=30, poll_frequency=1.0):
        """
        点击元素方法
        :param loc: 元素定位方法
        :param timeout: 等待时间
        :param poll_frequency: 间隔时长
        :return:
        """
        self.get_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=30, poll_frequency=1.0):
        """
        输入文本内容方法
        :param loc: 元素定位
        :param text: 输入文本
        :param timeout: 等待时长
        :param poll_frequency: 间隔时长
        :return:
        """
        element = self.get_element(loc,timeout,poll_frequency)
        element.clear()
        element.send_keys(text)
