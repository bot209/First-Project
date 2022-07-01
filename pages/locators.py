from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login_form"]/button')
    LOGIN_ALLERT_FAILED = (By.XPATH, '//*[@id="login_form"]/div[1]')
    LOGIN_ALLERT_SUCCESFUL = (By.CLASS_NAME, 'alertinner wicon')
    
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PASS_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')
    REG_ALLERT = (By.CSS_SELECTOR, '.alert-danger')
    REG_ALLERT_SUCCESS = (By.CSS_SELECTOR, '.alert-success')