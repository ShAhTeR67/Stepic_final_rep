from .pages.login_page import LoginPage


def test_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, url, 5)
    page.open()
    page.should_be_login_page()
