from .main_page import MainPage
from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'

    def should_be_login_url(self):                      # реализовать проверку на корректный url адрес
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'

    def should_be_login_form(self):                     # реализовать проверку, что есть форма логина
        link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys('loloalo@bk.ru')
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys('QaWsEd12345')
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        Failed = self.browser.find_element(*LoginPageLocators.LOGIN_ALLERT_FAILED).text
        assert Failed == "Опаньки! Мы нашли какие-то ошибки", 'Проверьте введеные данные в поле для авторизации'
    
    def should_be_register_form(self):                   # реализовать проверку, что есть форма регистрации на странице
        link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys('lfaaaololo@bk.ru')
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys('123456')
        self.browser.find_element(*LoginPageLocators.REG_PASS_2).send_keys('123456')
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
        Failed = self.browser.find_element(*LoginPageLocators.REG_ALLERT).text
        assert Failed == 'Опаньки! Мы нашли какие-то ошибки', 'Проверьте введеные данные в поле для регистрации'