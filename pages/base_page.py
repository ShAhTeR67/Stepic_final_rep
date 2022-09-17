from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, method, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout=timeout).until(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, method, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.browser.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def is_user_authorized(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User is not authorized. (User icon is absent)"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.CART_LINK)
        basket_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login button is absent"

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.CART_LINK), "Cart button is absent"

