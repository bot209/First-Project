from os import link
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                                 # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)        # Переход между страницами 
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
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