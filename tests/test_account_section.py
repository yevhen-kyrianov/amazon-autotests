

"""This module contains a test case for verifying the functionality of the account section
on the Amazon home page using Selenium WebDriver.
Fixtures:
    driver: A pytest fixture that initializes and provides a Selenium WebDriver instance
            configured with Chrome options and user-agent settings. The WebDriver is
            automatically closed after the test execution.
Test Cases:
    test_hover_account_section: Verifies that hovering over the account section on the
                                home page displays the "Sign In" button."""


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

 
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })

    yield driver
    driver.quit()

def test_hover_account_section(driver):
    home = HomePage(driver)
    home.open()
    home.hover_account_section()
    assert home.is_sign_in_button_displayed()