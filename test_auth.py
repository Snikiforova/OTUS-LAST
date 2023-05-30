import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login_page import LoginPage
from registration_page import RegistrationPage


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.opencart.com/index.php?route=account/login")
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture(scope="module")
def registration_page(driver):
    return RegistrationPage(driver)


def test_login_with_valid_credentials(driver, login_page):
    email = "test@example.com"
    password = "test_password"
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()
    assert login_page.check_login_success()

def test_login_with_invalid_credentials(driver, login_page):
    email = "invalid@example.com"
    password = "invalid_password"
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()
    assert not login_page.check_login_success()


def test_registration_with_valid_data(driver, registration_page):
    firstname = "Test"
    lastname = "User"
    email = "test@example.com"
    telephone = "1234567890"
    password = "test_password"
    registration_page.enter_firstname(firstname)
    registration_page.enter_lastname(lastname)
    registration_page.enter_email(email)
    registration_page.enter_telephone(telephone)
    registration_page.enter_password(password)
    registration_page.enter_password_confirm(password)
    registration_page.click_agree()
    registration_page.click_register_button()
    assert registration_page.check_registration_success()

def test_registration_with_invalid_data(driver, registration_page):
    firstname = ""
    lastname = ""
    email = "invalid_email"
    telephone = "invalid_phone"
    password = "test_password"
    registration_page.enter_firstname(firstname)
    registration_page.enter_lastname(lastname)
    registration_page.enter_email(email)
    registration_page.enter_telephone(telephone)
    registration_page.enter_password(password)
    registration_page.enter_password_confirm(password)
    registration_page.click_agree()
    registration_page.click_register_button()
    assert not registration_page.check_registration_success()