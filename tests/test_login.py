
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_login_navigation(driver):
    driver.get("https://www.amazon.ca")
    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)
    login.enter_email("fake@example.com")

@pytest.mark.smoke
def test_login_navigation(driver):
    driver.get("https://www.amazon.ca")

    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)
    login.enter_email("fakeemail@example.com")
    login.click_continue()

    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ap_password"))), "Password field not found"
    login.enter_password("fakepassword")