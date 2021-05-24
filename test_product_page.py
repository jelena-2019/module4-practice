import math

from pages.main_page import MainPage
from pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException


def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_price = product_page.get_product_price()
    product_page.add_product_to_basket()
    solve_quiz_and_get_code(product_page)
    product_page.check_product_message()
    product_page.check_added_product(product_price)
