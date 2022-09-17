from .base_page import BasePage
from .locators import BasketPageLocators
from .basket_empty_message import languages


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.browser.find_elements(*BasketPageLocators.BASKET_EMPTY), "Basket has products"

    def have_empty_message(self):
        basket_message_element = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        returned_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).get_attribute("href").split("/")
        message_language = returned_message[-2]
        expected_message = languages.get(message_language)
        basket_message = basket_message_element.text

        assert expected_message in basket_message, f"Received message '{basket_message}'" \
                                                   f" not equal to '{expected_message}'"
