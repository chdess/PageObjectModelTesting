from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REG_PASS)
        password_field.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.REG_PASS_CON)
        password_confirm.send_keys(password)
        registration_submit = self.browser.find_element(*LoginPageLocators.REG_SUBMIT)
        registration_submit.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login substring is not presented in this link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTH_FORM), "Login form is not presented on this page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Login form is not presented on this page"