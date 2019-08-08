# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for Login page locators. All main page locators should come here"""


class MainPageLocators(object):
    location_popup_allow = (By.XPATH, "//android.widget.Button[@text = 'ALLOW']")
    mainPage_title = (By.XPATH, "//android.widget.Button[@content-desc='tab, 1 of 4']")
    scroll_view = (By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")
    search_box = (By.XPATH, "//android.widget.EditText")


class SearchPanelLocators(object):
    first_hot_search =(By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]")


class SearchResultLocators(object):
    search_box = (By.XPATH, "//android.widget.EditText")





