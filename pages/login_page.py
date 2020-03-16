from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()

    def should_be_login_url(self):
        self.should_be_login_url()
        assert self.current_url("login"), "Login is not presented"
        assert True

    def should_be_login_form(self):
        self.should_be_login_form()
        assert self.is_element_present(By.CSS_SELECTOR, "#id_login-username_error"), "Login input is not presented"
        assert self.is_element_present(By.CSS_SELECTOR, "#id_login-password_error"), "Password input is not presented"
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form > button_error"), "Login button is not presented"
        assert True

    def should_be_register_form(self):
        self.should_be_register_form()
        assert self.is_element_present(By.CSS_SELECTOR, "#id_registration-email_error"), "Register input is not presented"
        assert self.is_element_present(By.CSS_SELECTOR, "#id_registration-password1_error"), "Password input is not presented"
        assert self.is_element_present(By.CSS_SELECTOR, "#id_registration-password2_error"), "Second password input is not presented"
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form > button_error"), "Register button is not presented"
        assert True