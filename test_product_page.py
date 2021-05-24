import math
import pytest

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
#from selenium.common.exceptions import NoAlertPresentException


def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    #try:
    #    alert2 = self.browser.switch_to.alert
    #    alert_text = alert2.text
    #    print(f"Your code: {alert_text}")
    #    alert2.accept()
    #except NoAlertPresentException:
    #    print("No second alert presented")


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    # getting product price
    product_price = product_page.get_product_price()
    # getting product title
    product_title = product_page.get_product_name()
    # adding the product to the basket
    product_page.add_product_to_basket()
    solve_quiz_and_get_code(product_page)
    product_page.check_product_message(product_title)
    product_page.check_product_price_in_basket(product_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.add_product_to_basket()
    product_page.no_success_message_expected()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.login_link_is_displayed()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    basket_page = BasketPage(browser, link)
    basket_page.check_no_items()
    basket_page.check_empty_basket_message()