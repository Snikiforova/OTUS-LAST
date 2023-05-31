import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver


def setUp(self):

    self.driver = webdriver.Chrome()

    self.driver.implicitly_wait(10)


class LoginPageTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):

        self.driver.quit()

    def test_login_page(self):

        driver = self.driver
        driver.get("http://127.0.0.1:8081/index.php?route=account/login")
        username = driver.find_element(By.ID, "input-email")
        password = driver.find_element(By.ID,"input-password")
        submit_button = driver.find_element(By.XPATH,"//input[@type='submit']")
        username.send_keys("test@example.com")
        password.send_keys("password123")
        submit_button.click()


        class LoginPageTest(unittest.TestCase):

            def setUp(self):
                firefox_options = webdriver.FirefoxOptions()
                firefox_options.add_argument("--headless")
                firefox_options.add_argument("--disable-gpu")
                self.driver = webdriver.Firefox(firefox_options=firefox_options,
                                                executable_path="C:\\tools\\geckodriver.exe")



                self.driver.implicitly_wait(10)

            def tearDown(self):

                self.driver.quit()

            def test_login_page(self):

                driver = self.driver
                driver.get("http://127.0.0.1:8081/index.php?route=account/login")
                username = driver.find_element_by_name("email")
                password = driver.find_element_by_name("password")
                submit_button = driver.find_element_by_xpath("//input[@type='submit']")
                username.send_keys("test@example.com")
                password.send_keys("password123")
                submit_button.click()
                self.assertTrue("Account Dashboard" in driver.title)
