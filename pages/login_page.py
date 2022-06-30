from .main_page import MainPage
from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators
import time

class LoginPage(BasePage):
    # def should_be_login_page(self):
    #     self.should_be_login_url()
    #     self.should_be_login_form()
    #     self.should_be_register_form()

    # def should_be_login_url(self):
    #     # реализуйте проверку на корректный url адрес
    #     assert True

    # def should_be_login_form(self):

    #     # реализуйте проверку, что есть форма логина
    #     assert True

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys('lolololo@bk.ru')
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys('123456')
        self.browser.find_element(*LoginPageLocators.REG_PASS_2).send_keys('123456')
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
        assert self.browser.find_element(*LoginPageLocators.REG_ALLERT).text == 'Опаньки!', 'ОШИБКА РЕГИСТРАЦИИ'
        time.sleep(5)