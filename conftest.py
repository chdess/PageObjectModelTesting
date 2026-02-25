import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser-name', action='store', default='Chrome', help='Choose browsers: chrome or firefox, comma-separated')
    parser.addoption('--language', action='store', default='en', help='Choose language, comma-separated')

def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames:
        opt_browsers = metafunc.config.getoption("--browser-name")
        browsers = [b.strip() for b in opt_browsers.split(",")]
        metafunc.parametrize("browser", browsers, indirect=True)
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.param
    user_language = request.config.getoption("--language")
    if browser_name == "chrome":
        print("\nstart browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart browser for test..")
        options = Options()
        options.add_experimental_option('intl.accept_languages', user_language)
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser-name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    print()
    browser.quit()

"""
@pytest.fixture(scope="session")
def full_text():
    full_text = []
    yield full_text
    print("\n=== Secret Message ===")
    print("".join(full_text))
    print("========================")
"""