"""统一入口类"""
from page.search_page import SearchPage
from page.setting_page import SettingPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_setting_page(self):
        """返回设置页面的对象"""
        return SettingPage(self.driver)

    def get_search_page(self):
        """返回搜索页面对象"""
        return SearchPage(self.driver)


