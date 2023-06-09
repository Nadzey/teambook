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
        self.urls = url
        self.header_logo = HeaderLocators.LOGO
        self.open_menu_button = HeaderLocators.OPEN_MENU_BUTTON
        self.onboarding_header = HeaderLocators.ONBOARDING_HEADER
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
        self.browser.get(self.urls)
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.user_menu))

    def is_header_logo_displayed(self):
        return self.browser.find_element(*self.header_logo).is_displayed()

    def click_on_header_logo(self):
        self.browser.find_element(*self.header_logo).click()

    def user_menu(self):
        return self.browser.find_element(*self.user_menu)

    def open_user_menu(self):
        self.browser.find_element(*self.open_menu_button).click()

    def onboarding_header(self):
        return self.browser.find_element(*HeaderLocators.ONBOARDING_HEADER)

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

    def header_elements(self):
        return self.browser.find_element(*self.header)

    def header_elements_text(self, number):
        elements = self.header_elements().find_elements(By.XPATH, "//a | //img | //button")
        return elements[number - 1].text


class UserMenu:
    def __init__(self, browser, url):
        self.browser = browser
        self.urls = url
        self.logout_button = HeaderLocators.LOGOUT_BUTTON
        self.header = HeaderLocators.HEADER
        self.user_menu = HeaderLocators.USER_MENU
        self.organization_link = HeaderLocators.ORGANIZATION_LINK
        self.header_instance = Header(browser, url)
        self.profile_link = HeaderLocators.PROFILE_LINK
        self.my_week_link = HeaderLocators.MY_WEEK_LINK

    def open_user_menu(self):
        self.header_instance.open_user_menu()

    def load(self):
        self.browser.get(self.urls)
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.user_menu))

    def organization_link_open(self):
        self.header_instance.open_user_menu()
        time.sleep(3)
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.organization_link))
        element.click()
        time.sleep(5)

    def user_menu_links_count(self):
        links = self.browser.find_elements(*self.user_menu)[0].find_elements(By.TAG_NAME, "a")
        return len(links)

    def user_menu_links(self):
        user_menu = self.browser.find_element(*self.user_menu)
        return user_menu.find_elements(By.TAG_NAME, "a") if user_menu else []

    def user_menu_link_text(self, number):
        elements = self.user_menu_links()
        return elements[number - 1].text

    def logout(self):
        self.header_instance.open_user_menu()
        time.sleep(3)
        self.browser.find_element(*self.logout_button).click()

    def my_week_link_open(self):
        self.header_instance.open_user_menu()
        time.sleep(3)
        self.browser.find_element(*self.my_week_link).click()
        time.sleep(5)

    def profile_link_open(self):
        self.header_instance.open_user_menu()
        time.sleep(3)
        self.browser.find_element(*self.profile_link).click()
        time.sleep(5)

class HelpMenu:
    def __init__(self, browser, url):
        self.browser = browser
        self.urls = url
        self.knowledge_base_link = HeaderLocators.KNOWLEDGE_BASE_LINK
        self.contact_us_link = HeaderLocators.CONTACT_US_LINK
        self.suggest_feature_link = HeaderLocators.SUGGEST_FEATURE_LINK
        self.product_road_map_link = HeaderLocators.PRODUCT_ROAD_MAP_LINK
        self.reop_onboarding_link = HeaderLocators.REOP_ONBOARD_LINK
        self.reop_did_you_know_link = HeaderLocators.REOP_DID_YOU_KNOW_LINK
        self.help_menu1 = HeaderLocators.HELP1
        self.header_instance = Header(browser, url)
        self.help_menu_button = HeaderLocators.HELP

    def load(self):
        self.browser.get(self.urls)
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.help_menu1))

    def click_help_menu(self):
        self.browser.find_element(*self.help_menu_button).click()

    def help_menu_links(self):
        help_menu = self.browser.find_element(*self.help_menu1)
        elements = help_menu.find_elements(By.TAG_NAME, "a") if help_menu else []
        print(f"Number of elements in help menu: {len(elements)}")
        print(f"Elements: {elements}")
        return elements

    def help_menu_link_text(self, number):
        elements = self.help_menu_links()
        return elements[number - 1].text

    def help_menu_links_count(self):
        return len(self.help_menu_links())
