from pages.base_page import BasePage
from pages.locators import *


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def login_link_is_displayed(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            "Login link is not present"
