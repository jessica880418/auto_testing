# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for Login page locators. All main page locators should come here"""
    login_title = (By.XPATH, "//android.widget.TextView[@text = '登录']")
    login_button = (By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/"
                              "android.view.ViewGroup[1]/android.widget.TextView[@text = '登录']")


class MainPageLocators(object):
    mainPage_title = (By.XPATH, "//android.widget.TextView[@text = '首页']")
    merchant_order = (By.XPATH, "//android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView")


class MerchantOrderListLocators(object):
    merchant_title = (By.XPATH, "//android.widget.TextView[@text = '商户订单']")
    merchant_order = (By.XPATH, "//android.widget.ScrollView")
    first_order = (By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]")


class MerchantOrderDetailLocators(object):
    merchant_title = (By.XPATH, "//android.widget.TextView[@text = '商户订单详情']")
