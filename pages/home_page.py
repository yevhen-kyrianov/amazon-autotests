
"""
home_page.py
This module defines the HomePage class, which represents the Amazon home page 
and provides methods to interact with its elements.
Classes:
    HomePage: A page object model (POM) class for the Amazon home page.
Attributes:
    SEARCH_BAR (tuple): Locator for the search bar element.
    SEARCH_BUTTON (tuple): Locator for the search button element.
Methods:
    search(query):
        Inputs a search query into the search bar and clicks the search button.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.amazon.ca/"
        self.account_section = (By.ID, "nav-link-accountList")
        self.sign_in_button = (By.CLASS_NAME, "nav-action-signin-button")
        self.login_link = (By.ID, "nav-link-accountList")
        self.search_field = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")

    def open(self):
        self.driver.get(self.url)
        
    def go_to_login_page(self):
        sign_in_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "nav-link-accountList")))
        sign_in_button.click()

    def hover_account_section(self):
        account_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "nav-link-accountList")))
        ActionChains(self.driver).move_to_element(account_element).perform()

    def is_sign_in_button_displayed(self):
        return self.driver.find_element(*self.sign_in_button).is_displayed()
    
    def search_for_item(self, item):
        self.driver.find_element(*self.search_field).send_keys(item)
        self.driver.find_element(*self.search_button).click()