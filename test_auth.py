from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.constants import BASE_URL

def test_login_with_valid_credentials(driver):
    driver.get(BASE_URL + "/index.php?route=account/login")
    login_page = LoginPage(driver)
    email = "test@example.com"
    password = "test_password"
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()
    assert login_page.check_login_success()

def test_login_with_invalid_credentials(driver):
    driver.get(BASE_URL + "/index.php?route=account/login")
    login_page = LoginPage(driver)
    email = "invalid@example.com"
    password = "invalid_password"
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login_button()
    assert not login_page.check_login_success()

def test_registration_with_valid_data(driver):
    driver.get(BASE_URL + "/index.php?route=account/register")
    registration_page = RegistrationPage(driver)
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

def test_registration_with_invalid_data(driver):
    driver.get(BASE_URL + "/index.php?route=account/register")
    registration_page = RegistrationPage(driver)
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