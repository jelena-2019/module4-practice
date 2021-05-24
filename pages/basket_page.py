from pages.base_page import BasePage
from pages.locators import *


class BasketPage(BasePage):
    def check_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty"

    def check_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Basket is not empty"
