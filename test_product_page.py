from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.parametrize('id', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason='В этом тесте баг')), 8 ,9])
def test_guest_can_add_product_to_basket(browser, id):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{id}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_success_msg_and_product_name()
    print("Names are equal")
    page.check_product_and_basket_price()
    print("Price are equal")

def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/'
    page = BasketPage(browser, link)
    page.open()
    page.guest_click_button_see_basket()
    page.in_basket_are_no_item()
    page.expect_text_that_the_basket_is_empty()