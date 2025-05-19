
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "ap_email")
        self.continue_button = (By.ID, "continue")
        self.password_field = (By.ID, "ap_password")
        self.sign_in_button = (By.ID, "signInSubmit")
        self.error_message = (By.CLASS_NAME, "a-alert-content")

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.email_field)).send_keys(email)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_field)).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()
        
    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.error_message)).text