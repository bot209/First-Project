from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    ADD_TO_BASKET = (By.XPATH, "//*[@class='btn-group']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login_form"]/button')
    LOGIN_ALLERT_FAILED = (By.XPATH, '//*[@id="login_form"]/div[1]')
    LOGIN_ALLERT_SUCCESFUL = (By.CLASS_NAME, 'alertinner wicon')
    
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PASS_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')
    REG_ALLERT = (By.CSS_SELECTOR, '.alert-danger')
    REG_ALLERT_SUCCESS = (By.CSS_SELECTOR, '.alert-success')

class ProductPageLocators():
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form>button[type^="submit"]')
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, '.product_main>h1')
    SUCCESS_MSG_ADD_PRODUCT_TO_BASKET_TEXT = (By.CSS_SELECTOR, '.alertinner>strong:nth-child(1)')
    PRICE_TEXT = (By.CSS_SELECTOR, '.product_main>.price_color')
    MESSAGE_PRICE_TEXT = (By.CSS_SELECTOR, '.alertinner>p>strong')
    PRODUCT_HAS_BEEN_ADDED_TEXT = (By.CSS_SELECTOR, '#messages .alert:nth-child(1)')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
    ITEM_BASKET_MESSAGE = (By.CSS_SELECTOR, '#basket_formset')
