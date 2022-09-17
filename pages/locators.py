from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, 'span > a')
    CART_LINK_INVALID = (By.CSS_SELECTOR, 'span > a_invalid')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.CLASS_NAME, 'price_color')


class BasketPageLocators:
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p a')
