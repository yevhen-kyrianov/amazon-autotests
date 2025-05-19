
"""
BasePage module provides a base class for Selenium-based page objects.
Classes:
    BasePage: A base class that encapsulates common web page interactions 
              such as opening a URL, waiting for elements, clicking elements, 
              and inputting text.
Methods:
    __init__(driver, timeout=10):
        Initializes the BasePage with a WebDriver instance and a default timeout.
    open(url):
        Opens the specified URL in the browser.
    wait_for_element(locator):
        Waits for an element to be visible on the page and returns it.
    click(locator):
        Waits for an element to be visible and clicks on it.
    input_text(locator, text):
        Waits for an element to be visible, clears its content, and inputs the specified text.
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)