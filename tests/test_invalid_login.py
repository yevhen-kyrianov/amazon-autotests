
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.negative
def test_invalid_login(driver):
    driver.get("https://www.amazon.ca")
    home = HomePage(driver)
    home.go_to_login_page()

    login = LoginPage(driver)
    login.enter_email("invalid_email@example.com")
    login.click_continue()

    error = login.get_error_message()
    assert "We cannot find an account with that email address" in error, "Error message not displayed as expected"
    assert "Please check your email address and try again." in error, "Error message not displayed as expected"