import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage

@pytest.mark.usefixtures("driver")
def test_homepage_banner(driver):
    home_page = HomePage(driver)
    driver.get("https://www.amazon.ca/")
    
    banner = driver.find_element(By.ID, "gw-desktop-herotator")  # ID может меняться
    assert banner.is_displayed(), "Main banner is not displayed!"