import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from faker import Faker


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_registration_form(self, firstname, lastname, telephone, email, password):
        self.driver.find_element(By.ID, "input-firstname").send_keys(firstname)
        self.driver.find_element(By.ID, "input-lastname").send_keys(lastname)
        self.driver.find_element(By.ID, "input-telephone").send_keys(telephone)
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.ID, "input-confirm").send_keys(password)

    def accept_terms_and_conditions(self):
        checkbox = self.driver.find_element(By.NAME, "agree")
        checkbox.click()

    def submit_registration_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "btn btn-primary").click()


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self, driver):
        driver.get("http://127.0.0.1:8081/index.php?route=account/logout")


class MainPage:  # положить товар в корзину
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[3]/button[1]').click()

    def open_cart(self):
        self.driver.find_element(By.XPATH, '//*[@id="cart"]/button').click()

    def checkout(self):
        self.driver.get("http://127.0.0.1:8081/index.php?route=checkout/checkout")


class CartPage:  # оформление товара в корзине
    def __init__(self, driver, faker):
        self.driver = driver
        self.faker = faker

    def click_register_account(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH,'//*[@id="collapse-checkout-option"]/div/div/div[1]/div[1]/label')))
        button.click()
        self.driver.find_element(By.ID, 'button-account').click()

    def click_guest_checkout(self):
        self.driver.find_element(By.XPATH,
                                 '//input[@value="guest"]').click()
        self.driver.find_element(By.CLASS_NAME, 'btn btn-primary').click()

    def fill_register_account(self):
        password = self.faker.password()
        address = self.faker.address().split(",")
        self.driver.find_element(By.ID, "input-payment-firstname").send_keys(self.faker.name())
        self.driver.find_element(By.ID, "input-payment-lastname").send_keys(self.faker.last_name())
        self.driver.find_element(By.ID, "input-payment-email").send_keys(self.faker.email())
        self.driver.find_element(By.ID, "input-payment-telephone").send_keys(self.faker.phone_number())
        self.driver.find_element(By.ID, "input-payment-company").send_keys(self.faker.company())
        self.driver.find_element(By.ID, "input-payment-address-1").send_keys(address[0])
        self.driver.find_element(By.ID, "input-payment-address-2").send_keys(address[1])
        self.driver.find_element(By.ID, "input-payment-city").send_keys(self.faker.city())
        self.driver.find_element(By.ID, "input-payment-postcode").send_keys(self.faker.postcode())
        country = Select(driver.find_element_by_id('input-payment-country'))
        country.select_by_index(random.randint(1, 259))
        region = Select(driver.find_element_by_id('input-payment-zone'))
        region.select_by_index(random.randint(3513, 3612))
        self.driver.find_element(By.ID, "input-payment-password").send_keys(password)
        self.driver.find_element(By.ID, "input-payment-confirm").send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="collapse-payment-address"]/div/div[3]/div/input[1]').click
        self.driver.find_element(By.ID, "button-register").click()

    def fill_guest_account(self):
        address = self.faker.address().split(",")
        self.driver.find_element(By.ID, "input-payment-firstname").send_keys(self.faker.name())
        self.driver.find_element(By.ID, "input-payment-lastname").send_keys(self.faker.last_name())
        self.driver.find_element(By.ID, "input-payment-email").send_keys(self.faker.email())
        self.driver.find_element(By.ID, "input-payment-telephone").send_keys(self.faker.phone_number())
        self.driver.find_element(By.ID, "input-payment-company").send_keys(self.faker.company())
        self.driver.find_element(By.ID, "input-payment-address-1").send_keys(address[0])
        self.driver.find_element(By.ID, "input-payment-address-2").send_keys(address[1])
        self.driver.find_element(By.ID, "input-payment-city").send_keys(self.faker.city())
        self.driver.find_element(By.ID, "input-payment-postcode").send_keys(self.faker.postcode())
        country = Select(driver.find_element_by_id('input-payment-country'))
        country.select_by_index(random.randint(1, 259))
        region = Select(driver.find_element_by_id('input-payment-zone'))
        region.select_by_index(random.randint(3513, 3612))
        self.driver.find_element(By.ID, "button-guest").click()


class ChangeCurrency:
    def __init__(self, driver):
        self.driver = driver

    def check_currency_changes(self):
        self.driver.find_element(By.CLASS_NAME, "btn btn-link dropdown-toggle").click()
        self.driver.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/button').click()
        price1 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/p[2]/text()')
        self.driver.find_element(By.CLASS_NAME, "btn btn-link dropdown-toggle").click()
        self.driver.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/button').click()
        price2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/p[2]/text()')
        self.driver.find_element(By.CLASS_NAME, "btn btn-link dropdown-toggle").click()
        self.driver.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[3]/button').click()
        price3 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/p[2]/text()')
        assert price1 != price2
        assert price1 != price3


@pytest.fixture(scope="module")
def faker():
    # Create a Faker instance
    return Faker()


@pytest.fixture(scope="module")
def driver():
    # Create a WebDriver instance using Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"  # Specify the actual path to the Chrome executable

    driver = webdriver.Chrome(executable_path="E:\Загрузки\chromedriver_win32 (2)\chromedriver.exe",
                              chrome_options=chrome_options)
    yield driver


def test_registration(faker, driver):
    name = faker.name()
    surname = faker.last_name()
    email = faker.email()
    phone_number = faker.phone_number()
    password = faker.password()

    registration_page = RegistrationPage(driver)
    driver.get("http://127.0.0.1:8081/index.php?route=account/register")

    registration_page.fill_registration_form(name, surname, phone_number, email, password)
    registration_page.accept_terms_and_conditions()
    registration_page.submit_registration_form()


def test_currency_changes(driver):  # проверка изменения цен
    changeCurrencyPage = ChangeCurrency(driver)
    changeCurrencyPage.check_currency_changes()


def test_login_logout(driver):
    loginPage = LoginPage(driver)
    logoutPage = LogoutPage(driver)

    driver.get("http://127.0.0.1:8081/index.php?route=account/login")  # loginPage
    loginPage.login("user@email.com", "password123")
    driver.get("http://127.0.0.1:8081/index.php?route=account/account")  # logoutPage
    logoutPage.logOut()


def test_registration_and_checkout(faker, driver):
    main_page = MainPage(driver)
    driver.get("http://127.0.0.1:8081/index.php?route=common/home")

    main_page.add_to_cart()
    main_page.open_cart()
    main_page.checkout()

    cartPage = CartPage(driver, faker)
    driver.get("http://127.0.0.1:8081/index.php?route=checkout/checkout")
    cartPage.click_register_account()
    cartPage.fill_register_account()


def test_guest_checkout(driver, faker):
    main_page = MainPage(driver)
    driver.get("http://127.0.0.1:8081/index.php?route=common/home")

    main_page.add_to_cart()
    main_page.open_cart()
    main_page.checkout()

    cartPage = CartPage(driver, faker)
    driver.get("http://127.0.0.1:8081/index.php?route=checkout/checkout")
    cartPage.click_guest_checkout()
    cartPage.fill_guest_account()
