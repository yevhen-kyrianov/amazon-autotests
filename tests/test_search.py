

"""This module contains a pytest test case for verifying the Amazon Today's Deals page.
Fixtures:
    driver: A pytest fixture that initializes a Selenium WebDriver instance with
            specific options and configurations for testing.
Test Cases:
    test_amazon_deals_page(driver):
        - Navigates to the Amazon Today's Deals page.
        - Verifies that the page title contains the word "Deals"."""
        
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

import pages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from selenium.webdriver.chrome.service import Service
from pages.search_results_page import SearchPage

# @pytest.fixture
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)

#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)

#     driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#         "source": """
#             Object.defineProperty(navigator, 'webdriver', {
#                 get: () => undefined
#             })
#         """
#     })

#     yield driver
#     driver.quit()


def test_amazon_deals_page(driver):
    driver.get("https://www.amazon.ca/gp/goldbox")  # Amazon Today's Deals
    assert "Deals" in driver.title

def test_search(driver):
    driver.get("https://www.amazon.ca/")
    search_query = "laptop"
    SearchPage.enter_serch_query(search_query)
    SearchPage.click_continue()
    # Wait for the search results page to load
    
    # Verify that the search query is present in the URL after the search
    assert search_query in driver.current_url, f"Search query '{search_query}' not found in URL: {driver.current_url}"

@pytest.mark.smoke
def test_search_logo(driver):
    driver.get("https://www.amazon.ca/")
    page = HomePage(driver)
    assert page.is_logo_visible(), "Amazon logo is not visible on the homepage."
    assert page.is_search_visible(), "Search bar is not visible on the homepage."