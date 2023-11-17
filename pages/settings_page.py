from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.settingsPageLocators import SettingsPageLocators
from urls import SETTINGS_SETTINGS_URL, REGISTER_URL
import time


class SettingsPage:
    def __init__(self, browser, url=SETTINGS_SETTINGS_URL):
        self.browser = browser
        self.url = url
        self.company_name_input = SettingsPageLocators.COMPANY_NAME_INPUT
        self.delete_p = SettingsPageLocators.DELETE_ORGANIZATION_P
        self.delete_button = SettingsPageLocators.DELETE_BUTTON
        self.delete_account_button = SettingsPageLocators.DELETE_ACCOUNT_BUTTON

    def load(self):
        wait = WebDriverWait(self.browser, 10)
        self.browser.get(self.url)
        wait.until(
            EC.presence_of_element_located(SettingsPageLocators.DELETE_ORGANIZATION_P))
        
    def close_getting_started(self):
        wait = WebDriverWait(self.browser, 10)
        close = wait.until(
            EC.element_to_be_clickable(SettingsPageLocators.GETTING_STARTED_CLOSE))
        close.click()

    def delete_company(self, company_name):
        wait = WebDriverWait(self.browser, 10)
        deleteP = wait.until(
            EC.element_to_be_clickable(SettingsPageLocators.DELETE_ORGANIZATION_P))
        deleteP.click()
        deleteButton = wait.until(EC.element_to_be_clickable(SettingsPageLocators.DELETE_BUTTON))
        deleteButton.click()
        self.browser.find_element(*self.company_name_input).send_keys(company_name)
        deleteAccountBtn = wait.until(EC.element_to_be_clickable(SettingsPageLocators.DELETE_ACCOUNT_BUTTON))
        deleteAccountBtn.click()
        wait.until(EC.url_to_be(url=REGISTER_URL))
