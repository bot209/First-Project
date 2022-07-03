from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time

# # Парсим язык сайта
# def pytest_addoption(parser):
#     parser.addoption('--language',
#                     action='store', 
#                     default=None,
#                     help="Choose user language")

# # Обьявляем браузер в данной фикстуре и передаем ее как параметр в наш тест
# @pytest.fixture(scope="function")
# def browser(request):
#     lang = request.config.getoption('language')
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': lang})
#     browser = webdriver.Chrome(options=options)

# # При запуске браузера на выбраном языке, в логах будет отображаться на каком языке запустился тест
#     if lang == f'{lang}':
#         print(f"\nStart chrome browser for '{lang}' language..")
#     elif lang == f'{lang}':
#         print(f"\nStart chrome browser for '{lang}' language..")
#     else:
#         raise pytest.UsageError('Language should be ru on en')
#     yield browser
#     print(f"\nQuit chrome browser for '{lang}' language..")
#     browser.quit()

@pytest.fixture(scope='function')
def browser():
    print('\n Запускаю браузер...')
    browser = webdriver.Chrome()
    yield browser
    print('\n Закрываю браузер...')
    browser.quit()