from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import ProductPageLocators

class BasketPage(BasePage):
    def open_basket(self):
        try:
            self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
        except NoSuchElementException:
            return False
        return True

    def is_basket_empty(self):
        try:
            self.browser.find_element(*ProductPageLocators.EMPTY_BASKET_MESSAGE)
            result = True
        except NoSuchElementException:
            result = False
        assert result is True, 'Basket is not empty'