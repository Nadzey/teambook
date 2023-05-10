from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from tests.plannersPageLacators import PlannersPageLocators
from selenium.webdriver.support import expected_conditions as EC
import time


class PlannersPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.header_logo = PlannersPageLocators.LOGO
        self.logout_button = PlannersPageLocators.LOGOUT_BUTTON
        self.open_menu_button = PlannersPageLocators.OPEN_MENU_BUTTON
        self.onboarding_header = PlannersPageLocators.ONBOARDING_HEADER
        self.organization_link = PlannersPageLocators.ORGANIZATION_LINK

    def load(self):
        self.browser.get(self.url)
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.open_menu_button))

    def is_header_logo_displayed(self):
        return self.browser.find_element(*self.header_logo).is_displayed()

    def logout(self):
        self.browser.find_element(*self.open_menu_button).click()
        self.browser.find_element(*self.logout_button).click()

    def onboarding_header(self):
        return self.browser.find_element(*PlannersPageLocators.ONBOARDING_HEADER)

    def organization_link_open(self):
        self.browser.find_element(*self.open_menu_button).click()
        time.sleep(5)
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.organization_link))
        element.click()
        time.sleep(5)
