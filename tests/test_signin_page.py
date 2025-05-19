import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.signin_page import SignInPage

@pytest.mark.smoke
def test_signin_page_opens(driver):
    driver.get("https://www.amazon.ca/ap/signin")
    signin_page = SignInPage(driver)
    
    # Проверяем, что поле ввода email существует
    assert driver.find_element(*signin_page.email_field).is_displayed()