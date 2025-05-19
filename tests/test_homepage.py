

"""
This module contains a test case for verifying the Amazon homepage.
Classes:
    None
Functions:
    driver() -> WebDriver:
        A pytest fixture that initializes a Chrome WebDriver instance, maximizes the browser window,
        and ensures proper cleanup after the test execution.
    test_amazon_home_page(driver):
        Tests the Amazon homepage by verifying the page title, search bar visibility, and logo visibility.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_amazon_home_page(driver):
    driver.get("https://www.amazon.ca/")
    page = HomePage(driver)
    assert "Amazon.ca" in page.get_title()
    assert page.is_search_visible()
    assert page.is_logo_visible()