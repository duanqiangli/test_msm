import sys, os
import pytest
import yaml

from base.getFileData import GetFileData
from get_dir import BASE_DIR

sys.path.append(os.getcwd())

from base.get_driver import get_phone_driver
from page.page import Page



# [("1", "休眠"), ("m", "MAC地址"), ("w", "WLAN直连")]
def get_data():
    """获取测试数据"""
    data_list = []
    data = GetFileData().get_yaml_data("searchData.yaml")
    for i in data.values():
        data_list.append((i.get("text"), i.get("expect")))

    return data_list


class TestSearch:
    def setup_class(self):
        """初始化浏览器和实例化页面对象"""
        self.driver = get_phone_driver('com.android.settings', '.Settings')
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        """关闭手机驱动对象"""
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def click_search_btn(self):
        """点击搜索按钮"""
        self.page_obj.get_setting_page().click_search_btn()

    @pytest.mark.parametrize("text,expect", get_data())
    def test_search_data(self, text, expect):
        """测试搜索数据"""
        self.page_obj.get_search_page().send_search_text(text)  # 输入搜索内容
        result = self.page_obj.get_search_page().get_search_result()  # 获取搜索结果
        assert expect in result
