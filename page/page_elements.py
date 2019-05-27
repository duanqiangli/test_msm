"""管理页面元素"""
from selenium.webdriver.common.by import By


class PageElement:
    # 设置页
    search_btn_id = (By.ID, "com.android.settings:id/search")  # 搜索按钮

    # 搜索页
    search_input_id = (By.ID, "android:id/search_src_text")  # 搜索输入框
    search_result_ids = (By.ID, "com.android.settings:id/title") # 搜索结果
