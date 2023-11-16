from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.loginPageLocators import LoginPageLocators
from urls import LOGIN_URL
import time
from selenium.common.exceptions import TimeoutException


class LoginPage:
    def __init__(self, browser, url=LOGIN_URL):
        self.browser = browser
        self.email_input = LoginPageLocators.EMAIL_INPUT
        self.password_input = LoginPageLocators.PASSWORD_INPUT
        self.login_button = LoginPageLocators.LOGIN_BUTTON
        self.url = url
        self.error_message = LoginPageLocators.ERROR_MESSAGE
        self.create_organization = LoginPageLocators.CREATE_ORGANIZATION_LINK


    def load(self):
        self.browser.get(self.url)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.email_input))


    def login(self, email, password):
        wait = WebDriverWait(self.browser, 10)
        self.browser.find_element(*self.email_input).send_keys(email)
        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.login_button).click()

        try:
        # Ожидаем успешного входа (URL содержит "planners")
            wait.until(EC.url_contains("planners"))
            print("Succesful login")
        except TimeoutException:
        # Если URL не содержит "planners", то считаем вход неуспешным
            print("Login failed")


    def get_error_message(self):
        return self.browser.find_element(*LoginPageLocators.ERROR_MESSAGE).text


    def create_new_organization(self):
        self.browser.find_element(*LoginPageLocators.CREATE_ORGANIZATION_LINK).click()
