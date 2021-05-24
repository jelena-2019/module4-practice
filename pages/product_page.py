from pages.base_page import BasePage
from pages.locators import *


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def check_product_price_in_basket(self, prod_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        price2 = basket_price.get_attribute('innerText').split()
        price = price2[2]
        assert price == prod_price, \
            "Product was not added to basket, price is 0"

    def get_product_price(self):
        price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price_element.text

    def get_product_name(self):
        product_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_element.text

    def check_product_message(self, product_name):
        msg = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE)
        assert msg is not None, \
            "Product added message is not displayed"
        name_displayed = msg.get_attribute('innerText')
        assert (product_name in name_displayed), "Product name is not displayed in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
            "Success message is present, but should not be"

    def no_success_message_expected(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
            "Success message is not expected, but it is there"
