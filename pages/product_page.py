from pages.base_page import BasePage
from pages.locators import *


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def check_added_product(self, prod_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        price2 = basket_price.get_attribute('innerText').split()
        price = price2[2]
        assert price == prod_price, \
            "Product was not added to basket, price is 0"

    def get_product_price(self):
        price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price_element.text

    def check_product_message(self):
        msg = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE)
        assert msg is not None, \
            "Product added message is not displayed"
