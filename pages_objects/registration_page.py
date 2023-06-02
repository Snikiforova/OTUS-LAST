from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver, email, password):
        super().__init__(driver)
        self.email = email
        self.password = password
        self.first_name = Faker().first_name()
        self.last_name = Faker().last_name()
        self.address1 = Faker().building_number() + ' ' + Faker().street_name()
        self.address2 = Faker().secondary_address()
        self.city = Faker().city()
        self.postcode = Faker().postcode()
        self.phone_number = Faker().phone_number()

    def click_my_account(self):
        my_account_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#top-links > ul > li.dropdown > a"))
        )
        my_account_link.click()

    def select_register_page(self):
        register_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href$='account/register.php']"))
        )
        register_link.click()

    def open(self):
        self.driver.get(self.URL)


    def fill_registration_form(self):
        first_name_input = self.driver.find_element(By.NAME, "firstname")
        last_name_input = self.driver.find_element(By.NAME, "lastname")
        email_input = self.driver.find_element(By.NAME, "email")
        telephone_input = self.driver.find_element(By.NAME, "telephone")
        password_input = self.driver.find_element(By.NAME, "password")
        confirm_input = self.driver.find_element(By.NAME, "confirm")
        agree_checkbox = self.driver.find_element(By.NAME, "agree")
        continue_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Continue']")

        first_name_input.send_keys(self.first_name)
        last_name_input.send_keys(self.last_name)
        email_input.send_keys(self.email)
        telephone_input.send_keys(self.phone_number)
        password_input.send_keys(self.password)
        confirm_input.send_keys(self.password)
        agree_checkbox.click()
        continue_button.click()
