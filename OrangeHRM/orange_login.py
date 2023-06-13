import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_valid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    username.send_keys("Admin")
    password.send_keys("admin123")
    login_button.click()
    time.sleep(5)


def test_login_invalid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    username.send_keys("Admin1")
    password.send_keys("admin123")
    login_button.click()
    time.sleep(5)


test_login_invalid()
#test_login_valid()
