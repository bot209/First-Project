import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage

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