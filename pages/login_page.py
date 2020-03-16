from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.should_be_login_url()
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        self.should_be_login_form()
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        self.should_be_register_form()
        # реализуйте проверку, что есть форма регистрации на странице
        assert True