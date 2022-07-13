from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import random
import time

def pytest_addoption(parser):
    parser.addoption('--language',
                    action='store', 
                    default=None,
                    help="Choose language: ru, en, es...")

@pytest.fixture(scope="function")
def browser(request):
    print('\n Start browser...')
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(20)
    yield browser
    print('\n Quit browser...')
    time.sleep(2)
    browser.quit()

@pytest.fixture(scope='function')
def generate_email():
    yield str(time.time()) + '@fakemail.org'

@pytest.fixture(scope='function')
def generate_password():
    code = random.getrandbits(128)
    yield '%032x' % code
