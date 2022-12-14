from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage(BasePage):
    def should_be_login_page(self,browser,url):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url #find_element(*LoginPageLocators.LOGIN_URL)
        assert login_url, "Login url not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"
        
    def register_new_user(self,email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_IN_FORM)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_IN_FORM1)
        password_field.send_keys(password)
        password_field_repeat = self.browser.find_element(*LoginPageLocators.PASSWORD_IN_FORM2)
        password_field_repeat.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click