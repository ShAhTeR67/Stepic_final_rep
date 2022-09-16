import pytest
from .pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize('link', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                  "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                  "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8",
                                  "?promo=offer9"
                                  ]
                         )
def test_guest_can_add_to_cart(browser, link):
    url = r'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'+link
    page = ProductPage(browser, url)
    page.open()
    page.should_be_added_correct_product()


@pytest.mark.xfail(reson='Negative test case. Should fail')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.is_not_visible_success_message_after_adding_product_to_basket()


@pytest.mark.xfail(reason='Negative test case. Should fail')
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.is_disappeared_success_message_after_adding_product_to_basket()


def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()
