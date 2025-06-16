from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver (Chrome)
driver = webdriver.Chrome()

# Test Case: Valid and Invalid Login
def test_login():
    driver.get("https://www.saucedemo.com/")
    
    # Valid credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert "inventory.html" in driver.current_url, "Valid login failed"
    print("Valid login: Success")
    
    # Logout
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    
    # Invalid credentials
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username and password do not match" in error, "Invalid login error not displayed"
    print("Invalid login: Success")

# Run test
try:
    test_login()
finally:
    driver.quit()