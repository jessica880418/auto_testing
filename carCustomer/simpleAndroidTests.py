# -*- coding: utf-8 -*-

import os
import unittest
from appium import webdriver
from carCustomer.pages import *


# Returns abs path relative to this file
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = PATH("../apps/carCustomer.apk")

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        main_page = MainPage(self.driver)

        main_page.handle_location_popup()



    def tearDown(self):
        self.driver.quit()

    def test_scroll(self):
        main_page = MainPage(self.driver)
        # 检查首页界面加载完成
       # assert main_page.is_title_matches()

        # 下滑首页
        main_page.scroll_view()

    def test_searchHotSearch(self):
        main_page = MainPage(self.driver)
        search_panel_page = SearchPanelPage(self.driver)
        search_result_page = SearchResultPage(self.driver)


        # 检查首页界面加载完成
        #assert main_page.is_title_matches()

        # 打开查找
        main_page.open_search_panel()

        # 点击第一个热门搜索“现车打蜡”
        search_panel_page.click_first_hotsearch()

        # 验证在"现车打蜡"的搜索结果页面
        assert search_result_page.is_search_result("现车打蜡")

