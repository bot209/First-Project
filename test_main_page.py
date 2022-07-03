from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.xfail(reason='BUG is found')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()
 
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason='BUG is found')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_message_is_disappeared()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/'
    page = BasketPage(browser, link)
    page.open()
    page.guest_click_button_see_basket()
    page.in_basket_are_no_item()
    page.expect_text_that_the_basket_is_empty()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)                              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                                                 # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)        # Переход между страницами 
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
    
def test_guest_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
  
def test_login_autorization_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()

def test_login_registration_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_register_form()