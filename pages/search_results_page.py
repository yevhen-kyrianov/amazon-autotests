from selenium.webdriver.common.by import By

class SearchPage:
    """
    This module defines the SearchPage class, which represents the Amazon search results page"""
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.ID, "twotabsearchtextbox")
        self.continue_button = (By.ID, "nav-search-submit-button")
        

    def enter_serch_query(self, serch_query):
        self.driver.find_element(*self.search_field).send_keys(serch_query)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()