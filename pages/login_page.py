from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):                      # реализовать проверку на корректный url адрес
        assert self.url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

    def should_be_login_form(self):                     # реализовать проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)
    
    def should_be_register_form(self):                  # реализовать проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.REG_FORM)

    def register_new_user(self, email,password):
        self.browser.get('http://selenium1py.pythonanywhere.com/ru/accounts/login/')
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()