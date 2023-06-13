from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(username, password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    username_field = WebDriverWait(driver, 10, poll_frequency=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))

    try:
        assert username_field.is_enabled(), f"Username field Disabled."
        username_field.send_keys("Admin")
        print("Username field Enabled. Enter username")
    except Exception as e:
        print("Username field Exception: ", type(e).__name__)

    password_field = WebDriverWait(driver, 10, poll_frequency=2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))

    try:
        assert username_field.is_enabled(), f"Username field Disabled."
        password_field.send_keys("admin123")
        print("Password field Enabled. Enter password")
    except Exception as e:
        print("Password field Exception: ", type(e).__name__)

    try:
        login_button = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))
        login_button.click()
    except Exception as e:
        print("Login button Exception: ", type(e).__name__)


test_login("Admin", "admin123")
