from carCompany.locators import *


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """Home page action methods come here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        self.driver.implicitly_wait(3)
        login_title = self.driver.find_element(
            *LoginPageLocators.login_title)

        return login_title.is_displayed()

    def click_login_button(self):
        """Triggers the search"""
        login_button = self.driver.find_element(
            *LoginPageLocators.login_button)
        login_button.click()
        self.driver.implicitly_wait(2)

class MainPage(BasePage):
    """Home page action methods come here."""
    def is_title_matches(self):
        mainPage_title = self.driver.find_element(
            *MainPageLocators.mainPage_title)
        return mainPage_title.is_displayed()

    def click_merchant_order(self):
        """Triggers the search"""
        merchant_order = self.driver.find_element(
            *MainPageLocators.merchant_order)
        merchant_order.click()
        merchant_order.click()
        self.driver.implicitly_wait(2)


class MerchantOrderListPage(BasePage):
    """Home page action methods come here."""
    def is_title_matches(self):
        merchant_title = self.driver.find_element(
            *MerchantOrderListLocators.merchant_title)
        return merchant_title.is_displayed()

    def click_first_order(self):
        """Triggers the search"""
        first_order = self.driver.find_element(
            *MerchantOrderListLocators.first_order)
        first_order.click()
        self.driver.implicitly_wait(1)

class MerchantOrderDetailPage(BasePage):
    """Home page action methods come here."""
    def is_title_matches(self):
        merchant_title = self.driver.find_element(
            *MerchantOrderDetailLocators.merchant_title)
        return merchant_title.is_displayed()

