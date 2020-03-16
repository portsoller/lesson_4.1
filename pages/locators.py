from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
	LOGIN_INPUT = (By.CSS_SELECTOR, "#id_login-username")
	LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
	LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
	REGISTER_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
	REPEAT_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
