from carCustomer.locators import *
from appium.webdriver.common.touch_action import TouchAction


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


#
# class LoginPage(BasePage):
#     """Home page action methods come here."""
#
#     def is_title_matches(self):
#         """Verifies that the hardcoded text "Python" appears in page title"""
#         self.driver.implicitly_wait(3)
#         login_title = self.driver.find_element(
#             *LoginPageLocators.login_title)
#
#         return login_title.is_displayed()
#
#     def click_login_button(self):
#         """Triggers the search"""
#         login_button = self.driver.find_element(
#             *LoginPageLocators.login_button)
#         login_button.click()
#         self.driver.implicitly_wait(2)

class MainPage(BasePage):
    """Home page action methods come here."""

    def handle_location_popup(self):
        self.driver.implicitly_wait(5)
        location_popup_allow = self.driver.find_element(
            *MainPageLocators.location_popup_allow)
        location_popup_allow.click()

    def is_title_matches(self):
        self.driver.implicitly_wait(10)
        mainPage_title = self.driver.find_element(
            *MainPageLocators.mainPage_title)
        return mainPage_title.is_displayed()

    def scroll_view(self):
        # def scroll_page(self):
        #     action = TouchAction(self)
        #     action.press(BrowsePageElements.firs_element_to_scroll(self)).
        #     move_to(BrowsePageElements.second_element_to_scroll(self)).perform()
        self.driver.implicitly_wait(10)
        for i in range(0, 30):
            self.driver.swipe(100, 700, 100, 5)

    def open_search_panel(self):
        search_box = self.driver.find_element(
            *MainPageLocators.search_box)
        search_box.click()


class SearchPanelPage(BasePage):
    def click_first_hotsearch(self):
        first_hot_search = self.driver.find_element(
            *SearchPanelLocators.first_hot_search)
        action = TouchAction(self.driver)
        action.tap(x=100,y=500).perform()
        action.tap(x=100, y=500).perform()
        self.driver.implicitly_wait(1)


class SearchResultPage(BasePage):
    def is_search_result(self, keyword):
        search_box = self.driver.find_element(
            *SearchResultLocators.search_box)
        return search_box.text == keyword

