from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LoginPageLocators, RegistrationPageLocators, CartPageLocators, CheckoutPageLocators, SearchPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    def enter_email(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def check_login_success(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_SUCCESS_MESSAGE))
        return True

class RegistrationPage(BasePage):
    def enter_firstname(self, firstname):
        self.driver.find_element(*RegistrationPageLocators.FIRSTNAME_INPUT).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(*RegistrationPageLocators.LASTNAME_INPUT).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_telephone(self, telephone):
        self.driver.find_element(*RegistrationPageLocators.TELEPHONE_INPUT).send_keys(telephone)

    def enter_password(self, password):
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)

    def enter_password_confirm(self, password):
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_CONFIRM_INPUT).send_keys(password)

    def click_agree(self):
        self.driver.find_element(*RegistrationPageLocators.AGREE_CHECKBOX).click()

    def click_register_button(self):
        self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

    def check_registration_success(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_SUCCESS_MESSAGE))
        return True

class CartPage(BasePage):
    def click_cart_button(self):
        self.driver.find_element(*CartPageLocators.CART_BUTTON).click()

    def check_cart_items(self, item_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CartPageLocators.CART_ITEM_NAME))
        cart_item_name = self.driver.find_element(*CartPageLocators.CART_ITEM_NAME).text
        return item_name in cart_item_name

    def click_checkout_button(self):
        self.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()

class CheckoutPage(BasePage):
    def enter_firstname(self, firstname):
        self.driver.find_element(*CheckoutPageLocators.FIRSTNAME_INPUT).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(*CheckoutPageLocators.LASTNAME_INPUT).send_keys(lastname)

    def enter_email(self, email):
        self.driver.find_element(*CheckoutPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_telephone(self, telephone):
        self.driver.find_element(*CheckoutPageLocators.TELEPHONE_INPUT).send_keys(telephone)

    def enter_address(self, address):
        self.driver.find_element(*CheckoutPageLocators.ADDRESS_INPUT).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element(*CheckoutPageLocators.CITY_INPUT).send_keys(city)

    def enter_postcode(self, postcode):
        self.driver.find_element(*CheckoutPageLocators.POSTCODE_INPUT).send_keys(postcode)

    def select_country(self, country):
        self.driver.find_element(*CheckoutPageLocators.COUNTRY_SELECT).send_keys(country)

    def select_region(self, region):
        self.driver.find_element(*

Yuki Witch, [31.05.2023 14:01]
CheckoutPageLocators.REGION_SELECT).send_keys(region)

    def click_continue_button(self):
        self.driver.find_element(*CheckoutPageLocators.CONTINUE_BUTTON).click()

    def check_checkout_success(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CheckoutPageLocators.CHECKOUT_SUCCESS_MESSAGE))
        return True

class SearchPage(BasePage):
    def enter_search_query(self, query):
        self.driver.find_element(*SearchPageLocators.SEARCH_INPUT).send_keys(query)

    def click_search_button(self):
        self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON).click()

    def check_search_results(self, item_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SearchPageLocators.SEARCH_RESULTS_HEADER))
        search_results_header = self.driver.find_element(*SearchPageLocators.SEARCH_RESULTS_HEADER).text
        return item_name in search_results_header