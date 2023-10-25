from tests.registerPageLocators import RegisterPageLocators
from urls import REGISTER_URL
import time
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:
    def __init__(self, browser, url=REGISTER_URL):
        self.browser = browser
        self.first_name_input = RegisterPageLocators.FIRST_NAME_INPUT
        self.last_name_input = RegisterPageLocators.LAST_NAME_INPUT
        self.company_name_input = RegisterPageLocators.COMPANY_NAME_INPUT
        self.reg_email_input = RegisterPageLocators.REG_EMAIL_INPUT
        self.reg_password_input = RegisterPageLocators.REG_PASSWORD_INPUT
        self.agree_checkbox = RegisterPageLocators.AGREE_CHECKBOX
        self.create_organization_button = RegisterPageLocators.CREATE_ORGANIZATION_BUTTON
        self.url = url

    def load(self):
        self.browser.get(self.url)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.reg_email_input))

    def fill_form(self, first_name, last_name, company_name, email, password):
        first_name_input = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_INPUT)
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = self.browser.find_element(*RegisterPageLocators.LAST_NAME_INPUT)
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        company_name_input = self.browser.find_element(*RegisterPageLocators.COMPANY_NAME_INPUT)
        company_name_input.clear()
        company_name_input.send_keys(company_name)

        reg_email_input = self.browser.find_element(*RegisterPageLocators.REG_EMAIL_INPUT)
        reg_email_input.clear()
        reg_email_input.send_keys(email)

        reg_password_input = self.browser.find_element(*RegisterPageLocators.REG_PASSWORD_INPUT)
        reg_password_input.clear()
        reg_password_input.send_keys(password)

    def accept_terms(self):
        agree_checkbox = self.browser.find_element(*RegisterPageLocators.AGREE_CHECKBOX)
        agree_checkbox.click()

    def create_organization(self):
        create_organization_button = self.browser.find_element(*RegisterPageLocators.CREATE_ORGANIZATION_BUTTON)
        create_organization_button.click()
        time.sleep(3)

    def skip(self):
        skip_p = self.browser.find_element(*RegisterPageLocators.SKIP_P)
        skip_p.click()
        time.sleep(3)

    def get_error_message(self):
        error_message = self.browser.find_element(*RegisterPageLocators.ERROR_MESSAGE).text
        return error_message
