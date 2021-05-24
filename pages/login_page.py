from pages.base_page import BasePage
from pages.locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.login_url_is_correct()
        self.should_be_login_form()
        self.should_be_register_form()

    def login_url_is_correct(self):
        assert "login" in self.browser.current_url, "URL of the page is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not displayed"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not displayed"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_INPUT)
        password_input2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()
