from selenium.webdriver.common.by import By
import os
import sys

from pages_objects.main_page import MainPage

from pages_objects.cart_page import CartPage

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages_objects')))
sys.path.insert(0, '/path/to/pages_objects')


def test_login(driver):
    driver.get("http://127.0.0.1:8081/index.php?route=account/login")
    username = driver.find_element(By.ID, "input-email")
    password = driver.find_element(By.ID, "input-password")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    username.send_keys("test@example.com")
    password.send_keys("password123")
    submit_button.click()
    assert "Account Dashboard" in driver.title


def test_registration_and_checkout(driver, faker):
    main_page = MainPage(driver)
    driver.get("http://127.0.0.1:8081/index.php?route=common/home")
    main_page.add_to_cart()
    main_page.open_cart()
    main_page.checkout()
    cart_page = CartPage(driver, faker)
    driver.get("http://127.0.0.1:8081/index.php?route=checkout/checkout")
    cart_page.click_register_account()
    cart_page.fill_register_account()
