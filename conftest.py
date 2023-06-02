import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages_objects.registration_page import RegistrationPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox"
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://www.google.com",
        help="Enter base URL"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )
    parser.addoption(
        "--email",
        action="store",
        default="",
        help="Enter email for registration"
    )
    parser.addoption(
        "--password",
        action="store",
        default="",
        help="Enter password for registration"
    )


@pytest.fixture(scope="session")
def driver(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    driver = None
    if browser_name == "chrome":
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = Options()
        if headless:
            firefox_options.headless = True
        driver = webdriver.Firefox(options=firefox_options)

    driver.base_url = base_url
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def registration_page(driver, request):
    email = request.config.getoption("--email")
    password = request.config.getoption("--password")
    return RegistrationPage(driver, email, password)


@pytest.fixture(scope='module')
def buy_page(driver):
    page = BuyPage(driver)
    page.open()
    return page


@pytest.fixture(scope='module')
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page


@pytest.fixture(scope='module')
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page
