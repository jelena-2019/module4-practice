from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK_promo = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
