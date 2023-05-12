from selenium.webdriver.support.ui import WebDriverWait
from tests.headerLocators import HeaderLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from urls import ACTUALS_URL, PLANNERS_URL, USER_URL, DASHBOARD_URL, PROJECT_URL
from selenium.webdriver.common.action_chains import ActionChains


class Header:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.header_logo = HeaderLocators.LOGO
        self.logout_button = HeaderLocators.LOGOUT_BUTTON
        self.open_menu_button = HeaderLocators.OPEN_MENU_BUTTON
        self.onboarding_header = HeaderLocators.ONBOARDING_HEADER
        self.organization_link = HeaderLocators.ORGANIZATION_LINK
        self.planning_link = HeaderLocators.PLANNERS_LINK
        self.users_link = HeaderLocators.USER_LINK
        self.dashboard_link = HeaderLocators.DASHBOARD_LINK
        self.projects_link = HeaderLocators.PROJECT_LINK
        self.header_block = HeaderLocators.HEADER_BLOCK
        self.actuals_link = HeaderLocators.ACTUALS_LINK
        self.mui_dialog_close = HeaderLocators.MUI_DIALOG_CLOSE
        self.mui_dialog = HeaderLocators.MUI_DIALOG
        self.help_menu = HeaderLocators.HELP
        self.header = HeaderLocators.HEADER
        self.user_menu = HeaderLocators.USER_MENU

    def load(self):
        self.browser.get(self.url)
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.user_menu))

    def is_header_logo_displayed(self):
        return self.browser.find_element(*self.header_logo).is_displayed()

    def click_on_header_logo(self):
        self.browser.find_element(*self.header_logo).click()

    def open_user_menu(self):
        self.browser.find_element(*self.open_menu_button).click()

    def logout(self):
        self.open_user_menu()
        time.sleep(3)
        self.browser.find_element(*self.logout_button).click()

    def onboarding_header(self):
        return self.browser.find_element(*HeaderLocators.ONBOARDING_HEADER)

    def organization_link_open(self):
        self.open_user_menu()
        time.sleep(3)
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.organization_link))
        element.click()
        time.sleep(5)

    def header_links_block(self):
        return self.browser.find_element(*self.header_block)

    def header_block_links_count(self):
        return len(self.header_links_block().find_elements(By.TAG_NAME, "a"))

    def header_block_link_text(self, number):
        return self.header_links_block().find_elements(By.TAG_NAME, "a")[number - 1].text

    def click_planning_link(self):
        planning_link = self.browser.find_element(*self.planning_link)
        planning_link.click()
        WebDriverWait(self.browser, 15).until(EC.url_to_be(PLANNERS_URL))

    def click_actuals_link(self):
        actuals_link = self.browser.find_element(*self.actuals_link)
        actions = ActionChains(self.browser)
        actions.move_to_element(actuals_link).click()

        dialog = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((self.mui_dialog)))
        close_button = dialog.find_element(*self.mui_dialog_close)
        close_button.click()

        WebDriverWait(self.browser, 30).until(EC.url_to_be(ACTUALS_URL))

    def click_dashboard_link(self):
        dashboard_link = self.browser.find_element(*self.dashboard_link)
        dashboard_link.click()
        WebDriverWait(self.browser, 15).until(EC.url_to_be(DASHBOARD_URL))

    def click_users_link(self):
        users_link = self.browser.find_element(*self.users_link)
        users_link.click()
        WebDriverWait(self.browser, 15).until(EC.url_to_be(USER_URL))

    def click_projects_link(self, url=PROJECT_URL):
        projects_link = self.browser.find_element(*self.projects_link)
        projects_link.click()
        WebDriverWait(self.browser, 15).until(EC.url_to_be(url))

    def open_help_menu(self):
        self.browser.find_element(*self.help_menu).click()

    def verify_elements_present(self):
        assert self.browser.find_element(*self.header).is_displayed()
        assert self.browser.find_element(*self.header_logo).is_displayed()
        assert self.browser.find_element(*self.planning_link).is_displayed()
        assert self.browser.find_element(*self.actuals_link).is_displayed()
        assert self.browser.find_element(*self.dashboard_link).is_displayed()
        assert self.browser.find_element(*self.users_link).is_displayed()
        assert self.browser.find_element(*self.projects_link).is_displayed()
        assert self.browser.find_element(*self.help_menu).is_displayed()
        assert self.browser.find_element(*self.open_menu_button).is_displayed()

    def header_elements_text(self, number):
        elements = self.header().find_elements(By.XPATH, "//a | //img | //button")
        return elements[number - 1].text

    def user_menu_links_count(self):
        return len(self.user_menu().find_elements(By.TAG_NAME, "a"))

    def user_menu_link_text(self, number):
        return self.user_menu().find_elements(By.TAG_NAME, "a")[number - 1].text
