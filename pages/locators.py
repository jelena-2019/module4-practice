from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK_promo = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.XPATH, "//a[contains(.,'View basket')]")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(.,'Your basket is empty')]")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
