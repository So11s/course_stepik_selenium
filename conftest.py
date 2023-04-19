import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FireFoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
    help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help='Select language for browser')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FireFoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
