"""搜索页面"""
from base.base import Base
from page.page_elements import PageElement


class SearchPage(Base):
    def __init__(self, driver):
        """传入driver"""
        Base.__init__(self, driver)

    def send_search_text(self, text):
        """输入搜索内容"""
        self.send_element(PageElement.search_input_id, text)

    def get_search_result(self):
        """获取搜索结果"""
        result_list = self.get_elements(PageElement.search_result_ids)
        return [i.text for i in result_list]
