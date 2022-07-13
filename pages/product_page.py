from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_card(self)->bool:
        try:
            self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON).click()
            return True
        except NoSuchElementException:
            return False

    def get_product_name(self)->str:
        try:
            return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TEXT).text
        except NoSuchElementException:
            return None

    def get_success_message_after_add_product_to_basket(self)->str:
        WD(self.browser, 20).until(EC.presence_of_element_located(ProductPageLocators.SUCCESS_MSG_ADD_PRODUCT_TO_BASKET_TEXT))
        try:
            return self.browser.find_element(*ProductPageLocators.SUCCESS_MSG_ADD_PRODUCT_TO_BASKET_TEXT).text
        except NoSuchElementException:
            return None

    def get_price(self)-> str:
        try:
            return self.browser.find_element(*ProductPageLocators.PRICE_TEXT).text
        except NoSuchElementException:
            return None

    def get_price_from_message(self)-> str:
        WD(self.browser, 20).until(EC.presence_of_element_located(ProductPageLocators.MESSAGE_PRICE_TEXT))
        try:
            return self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_TEXT).text
        except NoSuchElementException:
            return None
    
    def check_product_name_on_page_and_in_message(self):
        success_msg = self.get_success_message_after_add_product_to_basket()
        product_name = self.get_product_name()
        assert success_msg == product_name, 'Product names are not equal'

    def check_price_on_page_and_in_message(self):
        product_price = self.get_price()
        basket_price = self.get_price_from_message()
        assert product_price == basket_price, 'Prices are not equal'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_TEXT)

    def should_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_TEXT)
    