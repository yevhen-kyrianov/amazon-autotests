from selenium.webdriver.common.by import By

class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "ap_email")
        self.continue_button = (By.ID, "continue")

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()