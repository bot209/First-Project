from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators

class BasketPage(BasePage):
    def in_basket_are_no_item(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_BASKET_MESSAGE)               # Ожидаем, что в корзине нет товаров

    def expect_text_that_the_basket_is_empty(self):                                                # Ожидаем, что есть текст о том что корзина пуста
        assert self.is_element_present(*ProductPageLocators.EMPTY_BASKET_MESSAGE)