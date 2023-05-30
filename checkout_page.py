from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def start_checkout(self):
        pass

    def enter_guest_details(self, firstname, lastname, email, phone):
        pass

    def enter_address_information(self, address, city, postcode, country, region):
        pass

    def click_delivery_options(self):
        pass

    def click_payment_method(self):
     pass

    def click_confirm_order_button(self):
        pass

    def check_order_success(self):
        pass
