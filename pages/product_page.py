import math

from .base_page import BasePage
from .locators import ProductPageLocators


def calc_alert(x: float):
    return str(math.log(abs(12 * math.sin(x))))


class ProductPage(BasePage):
    def should_be_added_correct_product(self):
        book_name = self.get_book_name()
        price = self.get_price()

        self.should_add_to_basket()

        self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        response_message = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)
        response_book_name = response_message[0].text
        response_cart_value = response_message[2].text

        assert book_name == response_book_name, f"Added book name '{response_book_name}' " \
                                                f"doesn't match original name '{book_name}'"

        assert price == response_cart_value, f"Added item price is '{response_cart_value}'" \
                                             f" but original price was '{price}'"

    def should_add_to_basket(self):
        self.is_element_present(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_btn.click()

        if self.should_be_alert():
            alert = self.browser.switch_to.alert
            x = alert.text.split(' ')
            ans = calc_alert(float(x[2]))
            alert.send_keys(ans)
            alert.accept()
        else:
            print("First alert didn't appear!")

        if self.should_be_alert():
            alert = self.browser.switch_to.alert
            ans = alert.text.split(' ')
            assert "Поздравляем" in ans[0], "Answer was wrong"
            alert.accept()
        else:
            print("No second alert appeared")

    def should_not_be_success_message_after_adding_product_to_basket(self):
        self.should_add_to_basket()
        self.should_not_be_success_message()

    def is_not_visible_success_message_after_adding_product_to_basket(self):
        self.should_not_be_success_message()

    def is_disappeared_success_message_after_adding_product_to_basket(self):
        self.should_add_to_basket()
        self.should_be_disappeared()

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_alert(self):
        return self.is_alert_present()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Element is present but should not"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message should disappear but it didn't"
