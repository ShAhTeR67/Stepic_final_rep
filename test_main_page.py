import pytest

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


@pytest.mark.login_from_main_page
class TestLoginFromMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.url = "http://selenium1py.pythonanywhere.com/"

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.url)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, self.url)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, url)
    page.open()
    page.go_to_basket_page()
    basket_page_url = page.browser.current_url
    basket_page = BasketPage(browser, basket_page_url)
    basket_page.is_basket_empty()
    basket_page.have_empty_message()
