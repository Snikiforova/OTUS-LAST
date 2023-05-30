from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.email_input = self.wait.until(EC.presence_of_element_located((By.ID, "input-email")))
        self.password_input = self.wait.until(EC.presence_of_element_located((By.ID, "input-password")))
        self.login_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.btn.btn-primary")))

    def enter_email(self, email):
        self.email_input.clear()
        self.email_input.send_keys(email)

    def enter_password(self, password):
        self.password_input.clear()
        self.password_input.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

    def check_login_success(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
            return True
        except:
            return False
