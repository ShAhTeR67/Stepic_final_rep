import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as FireFox_Options


# We could set default param e.g. default='chrome'
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox"
                     )
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru or en'
                     )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    # Creates custom options is chrome is chosen
    if browser_name == 'chrome':
        # Set options
        options = Chrome_Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        print('\nChrome browser instance is created')
    elif browser_name == 'firefox':
        # Set profile
        options = FireFox_Options()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
        print('\nFirefox browser instance is created')
    else:
        raise pytest.UsageError('No browser was selected. Please select "chrome" or "firefox"')

    # Closing browser after finishing test
    def quit_browser():
        browser.quit()
        print('\nBrowser instance is closed')

    request.addfinalizer(quit_browser)
    return browser
