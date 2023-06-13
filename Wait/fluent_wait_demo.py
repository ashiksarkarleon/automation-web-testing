from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_valid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        username = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
        username.send_keys("Admin")
    except Exception as e:
        print("Username field Exception: ", type(e).__name__)

    try:
        password = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
        password.send_keys("admin123")
    except Exception as e:
        print("Password field Exception: ", type(e).__name__)

    try:
        login_button = WebDriverWait(driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))
        login_button.click()
    except Exception as e:
        print("Login button Exception: ", type(e).__name__)


test_login_valid()
