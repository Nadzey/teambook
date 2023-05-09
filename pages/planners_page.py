from selenium.webdriver.common.by import By
from tests.plannersPageLacators import plannersPageLocators

class PlannersPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.header_logo = plannersPageLocators.LOGO
        self.logout_button = plannersPageLocators.LOGOUT_BUTTON
        self.open_menu_button = plannersPageLocators.OPEN_MENU_BUTTON

    def load(self):
        self.browser.get(self.url)

    def is_header_logo_displayed(self):
        return self.browser.find_element(*self.header_logo).is_displayed()

    def logout(self):
        self.browser.find_element(*self.open_menu_button).click()
        self.browser.find_element(*self.logout_button).click()
