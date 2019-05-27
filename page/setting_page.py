"""设置页页面"""
from base.base import Base
from page.page_elements import PageElement


class SettingPage(Base):
    def __init__(self,driver):
        """传入driver"""
        Base.__init__(self,driver)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_element(PageElement.search_btn_id)
