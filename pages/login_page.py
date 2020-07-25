from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import random


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert current_url == "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, i_password='Testpass1123'):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD).send_keys(str(random.getrandbits(25)) +
                                                                                         "@fake-email.org")
        self.write_field(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD, i_password)
        self.write_field(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD, i_password)
        self.click(*LoginPageLocators.REGISTRATION_BUTTON)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_COMPLETE_MESSAGE), \
            "Registration message is not presented"

    def register_new_user_with_not_valid_email(self, i_email='not-valid-email.org', i_password='Test-pass1123'):
        self.write_field(*LoginPageLocators.REGISTRATION_EMAIL_FIELD, i_email)
        self.write_field(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD, i_password)
        self.write_field(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD, i_password)
        self.click(*LoginPageLocators.REGISTRATION_BUTTON)
        assert not self.is_element_present(*LoginPageLocators.REGISTRATION_COMPLETE_MESSAGE), \
            "Whoops! Registration message presented"