from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self)->bool:
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
    def get_success_msg_add_product_to_basket(self)->str:
        WD(self.browser, 20).until(EC.presence_of_element_located(ProductPageLocators.SUCCESS_MSG_ADD_PRODUCT_TO_BASKET_TEXT))
        try:
            return self.browser.find_element(*ProductPageLocators.SUCCESS_MSG_ADD_PRODUCT_TO_BASKET_TEXT).text
        except NoSuchElementException:
            return None
    def get_product_price(self)-> str:
        try:
            return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_TEXT).text
        except NoSuchElementException:
            return None
    def get_basket_price_from_msg(self)-> str:
        WD(self.browser, 20).until(EC.presence_of_element_located(ProductPageLocators.BASKET_PRICE_TEXT))
        try:
            return self.browser.find_element(*ProductPageLocators.BASKET_PRICE_TEXT).text
        except NoSuchElementException:
            return None
    
    def check_success_msg_and_product_name(self):
        success_msg = self.get_success_msg_add_product_to_basket()
        product_name = self.get_product_name()
        assert success_msg == product_name, 'Product names are not equal'

    def check_product_and_basket_price(self):
        product_price = self.get_product_price()
        basket_price = self.get_basket_price_from_msg()
        assert product_price == basket_price, 'Product prices are not equal'