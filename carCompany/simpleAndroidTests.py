# -*- coding: utf-8 -*-

import os
import unittest
from carCompany.pages import *
from appium import webdriver


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
        desired_caps['app'] = PATH("../apps/carCompany.apk")

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)

        # 检查登录界面加载完成
        assert login_page.is_title_matches()

        # 点击登录
        login_page.click_login_button()

        # 验证跳转成功
        main_page.is_title_matches()


    def test_merchantOrderDetail(self):
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)
        merchantOrderList_page = MerchantOrderListPage(self.driver)
        merchantOrderDetail_page = MerchantOrderDetailPage(self.driver)

        # 检查登录界面加载完成
        assert login_page.is_title_matches()

        # 点击登录
        login_page.click_login_button()

        # 点击商户订单前往商户订单列表
        main_page.click_merchant_order()

        # 验证抵达商户订单列表
        merchantOrderList_page.is_title_matches()

        # 点击第一个订单
        merchantOrderList_page.click_first_order()

        # 验证进入订单详情
        merchantOrderDetail_page.is_title_matches()

