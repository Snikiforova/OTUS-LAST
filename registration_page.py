from selenium.webdriver.common.by import By


def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(self.driver, 10)
    self.firstname_input = self.wait.until(EC.presence_of_element_located((By.ID, "input-firstname")))
    self.lastname_input = self.wait.until(EC.presence_of_element_located((By.ID, "input-lastname")))
    self.email_input = self.wait.until(EC.presence_of_element_located((By.ID, "input-email")))
    self.telephone_input = self.wait.until(EC.presence_of_element_located((By.ID, "input-telephone")))
    self.password_input = self.wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    self.password_confirm_input = self.wait.until(EC.presence_of_element_located((By.ID, "input-confirm")))
    self.agree_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "agree")))
    self.register_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.btn.btn-primary")))


def enter_firstname(self, firstname):
    self.firstname_input.clear()
    self.firstname_input.send_keys(firstname)


def enter_lastname(self, lastname):
    self.lastname_input.clear()
    self.lastname_input.send_keys(lastname)


def enter_email(self, email):
    self.email_input.clear()
    self.email_input.send_keys(email)


def enter_telephone(self, telephone):
    self.telephone_input.clear()
    self.telephone_input.send_keys(telephone)


def enter_password(self, password):
    self.password_input.clear()
    self.password_input.send_keys(password)


def enter_password_confirm(self, password):
    self.password_confirm_input.clear()
    self.password_confirm_input.send_keys(password)


def click_agree(self):
    self.agree_checkbox.click()


def click_register_button(self):
    self.register_button.click()


def check_registration_success(self):
    try:
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
        return True
    except:
        return False