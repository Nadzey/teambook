from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.loginPageLocators import LoginPageLocators
from urls import LOGIN_URL


class LoginPage:
    def __init__(self, browser, url=LOGIN_URL):
        self.browser = browser
        self.email_input = LoginPageLocators.EMAIL_INPUT
        self.password_input = LoginPageLocators.PASSWORD_INPUT
        self.login_button = LoginPageLocators.LOGIN_BUTTON
        self.url = url

    def load(self):
        self.browser.get(self.url)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.email_input))

    def login(self, email, password):
        self.browser.find_element(*self.email_input).send_keys(email)
        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.login_button).click()
