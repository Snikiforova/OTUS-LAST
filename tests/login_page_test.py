import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def setUp(self):

    self.driver = webdriver.Chrome()  # Для Chrome

    self.driver.implicitly_wait(10)

class LoginPageTest(unittest.TestCase):

class LoginPageTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):

        self.driver.quit()

    def test_login_page(self):
        # Тестовый метод
        driver = self.driver
        driver.get("https://www.opencart.com/index.php?route=account/login")
        username = driver.find_element_by_name("email")
        password = driver.find_element_by_name("password")
        submit_button = driver.find_element_by_xpath("//input[@type='submit']")
        username.send_keys("test@example.com")
        password.send_keys("password123")
        submit_button.click()
        self.assertTrue("Account Dashboard" in driver.title)

        class LoginPageTest(unittest.TestCase):

            def setUp(self):
                firefox_options = webdriver.FirefoxOptions()
                firefox_options.add_argument("--headless")
                firefox_options.add_argument("--disable-gpu")
                self.driver = webdriver.Firefox(firefox_options=firefox_options,
                                                executable_path="C:\\tools\\geckodriver.exe")

                 Для Edge на Windows 10:
                self.driver = webdriver.Edge(executable_path="C:\\tools\\MicrosoftWebDriver.exe")

                self.driver.implicitly_wait(10)

            def tearDown(self):

                self.driver.quit()

            def test_login_page(self):

                driver = self.driver
                driver.get("https://www.opencart.com/index.php?route=account/login")
                username = driver.find_element_by_name("email")
                password = driver.find_element_by_name("password")
                submit_button = driver.find_element_by_xpath("//input[@type='submit']")
                username.send_keys("test@example.com")
                password.send_keys("password123")
                submit_button.click()
                self.assertTrue("Account Dashboard" in driver.title)
