import time
import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.user_can_add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.url = r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()).split('.')[0]

        self.page = ProductPage(browser, self.url)
        self.page.open()
        self.page.go_to_login_page()

        login_page_url = self.page.browser.current_url
        self.login_page = LoginPage(browser, login_page_url)
        self.login_page.register_new_user(email, password)
        self.login_page.is_user_authorized()

    @pytest.mark.need_review
    def test_user_can_add_to_cart(self, browser):
        self.page.open()
        self.page.should_be_added_correct_product()

    def test_user_cant_see_success_message(self, browser):
        self.page.open()
        self.page.is_not_visible_success_message_after_adding_product_to_basket()


@pytest.mark.login_from_product_page
class TestLoginFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.url = "http://selenium1py.pythonanywhere.com/"

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.url)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.url)
        page.open()
        page.should_be_login_link()


@pytest.mark.basket_from_product_page
class TestBasketFromProductPage:
    @pytest.mark.need_review
    @pytest.mark.parametrize("link", ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                      "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                      "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8",
                                      "?promo=offer9"
                                      ]
                             )
    def test_guest_can_add_to_cart(self, browser, link):
        url = r"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"+link
        page = ProductPage(browser, url)
        page.open()
        page.should_be_added_correct_product()

    def test_guest_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.is_not_visible_success_message_after_adding_product_to_basket()

    @pytest.mark.xfail(reson="Negative test case. Should fail because success message appear")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message_after_adding_product_to_basket()

    @pytest.mark.xfail(reason="Negative test case. Should fail because message don't disappear")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.is_disappeared_success_message_after_adding_product_to_basket()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/ru/"
        page = ProductPage(browser, url)
        page.open()
        page.go_to_basket_page()
        basket_page_url = page.browser.current_url
        basket_page = BasketPage(browser, basket_page_url)
        basket_page.is_basket_empty()
        basket_page.have_empty_message()
