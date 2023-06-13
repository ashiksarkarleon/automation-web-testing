from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(username, password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    try:
        assert "OrangeHRM" in driver.title, f"It's not Login page. Title Mismatch"
        print("Login page Open Successful.")
        try:
            username_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
            username_field.send_keys(username)
        except Exception as e:
            print("Username field Exception: ", type(e).__name__)

        try:
            password_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
            password_field.send_keys(password)
        except Exception as e:
            print("Password field Exception: ", type(e).__name__)

        try:
            login_button = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))
            login_button.click()
        except Exception as e:
            print("Login button Exception: ", type(e).__name__)

    except Exception as e:
        print("Login page Exception: ", type(e).__name__)


test_login("Admin", "admin123")
