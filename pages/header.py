from selenium.webdriver.support.ui import WebDriverWait
from tests.headerLocators import HeaderLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from urls import ACTUALS_URL, PLANNERS_URL, USER_URL, DASHBOARD_URL, PROJECT_URL


class Header:
    def __init__(self, browser, url):
        self.browser = browser
        self.urls = url
        self.header_logo = HeaderLocators.LOGO
        self.open_menu_button = HeaderLocators.OPEN_MENU_BUTTON
        self.onboarding_header1 = HeaderLocators.ONBOARDING_HEADER
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
        self.user_menu1 = HeaderLocators.USER_MENU
        self.getting_start = HeaderLocators.GETTING_STARTED
        self.background = HeaderLocators.BACKGROUND
        self.logout_button = HeaderLocators.LOGOUT_BUTTON

    def load(self):
        self.browser.get(self.urls)
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.header_logo))

    def is_header_logo_displayed(self):
        return self.browser.find_element(*self.header_logo).is_displayed()

    def click_on_header_logo(self):
        wait = WebDriverWait(self.browser, 10)
        header_logo = wait.until(EC.element_to_be_clickable(self.header_logo))
        header_logo.click()
        time.sleep(3)

    def close_getting_started(self):
        wait = WebDriverWait(self.browser, 10)
        self.browser.find_element(*self.getting_start).click()

    def user_menu(self):
        wait = WebDriverWait(self.browser, 10)
        return self.browser.find_element(*self.user_menu1)

    def open_user_menu(self):
        wait = WebDriverWait(self.browser, 10)
        user_menu_button = wait.until(EC.element_to_be_clickable(self.open_menu_button))
        user_menu_button.click()
        time.sleep(3)

    def click_help_menu(self):
        wait = WebDriverWait(self.browser, 10)
        help_menu = wait.until(EC.element_to_be_clickable(self.help_menu))
        help_menu.click()

    def onboarding_header(self):
        wait = WebDriverWait(self.browser, 10)
        onboarding = wait.until(EC.visibility_of_element_located(self.onboarding_header1))
        return onboarding

    def header_links_block(self):
        wait = WebDriverWait(self.browser, 10)
        header_block = wait.until(EC.visibility_of_element_located(self.header_block))
        return header_block

    def header_block_links_count(self):
        return len(self.header_links_block().find_elements(By.TAG_NAME, "a"))

    def header_block_link_text(self, number): 
        wait = WebDriverWait(self.browser, 20)
        wait.until(EC.visibility_of_element_located(self.header_block))
        elements = self.header_links_block().find_elements(By.TAG_NAME, "a")
        return elements[number - 1].text.strip()
    

    def click_planning_link(self):
        wait = WebDriverWait(self.browser, 10)
        planning_link = wait.until(EC.element_to_be_clickable(self.planning_link))
        planning_link.click()
        wait.until(EC.url_to_be(PLANNERS_URL))

    def click_actual_link(self):
        wait = WebDriverWait(self.browser, 10)
        actual_link = wait.until(EC.element_to_be_clickable(self.actuals_link))
        actual_link.click()
        dialog = wait.until(
            EC.visibility_of_element_located((self.mui_dialog_close)))
        dialog.click()
        wait.until(EC.url_to_be(ACTUALS_URL))
        

    def click_dashboard_link(self):
        wait = WebDriverWait(self.browser, 10)
        dashboard_link = wait.until(EC.element_to_be_clickable(self.dashboard_link))
        dashboard_link.click()
        wait.until(EC.url_to_be(DASHBOARD_URL))

    def click_users_link(self):
        wait = WebDriverWait(self.browser, 10)
        users_link = wait.until(EC.element_to_be_clickable(self.users_link))
        users_link.click()
        wait.until(EC.url_to_be(USER_URL))

    def click_projects_link(self, url=PROJECT_URL):
        wait = WebDriverWait(self.browser, 10)
        projects_link = wait.until(EC.element_to_be_clickable(self.projects_link))
        projects_link.click()
        wait.until(EC.url_to_be(PROJECT_URL))

    def open_help_menu(self):
        wait = WebDriverWait(self.browser, 10)
        element = wait.until(EC.element_to_be_clickable(self.help_menu))
        element.click()

    def verify_elements_present(self):
        wait = WebDriverWait(self.browser, 10)
        assert self.browser.find_element(*self.header).is_displayed()
        assert self.browser.find_element(*self.header_logo).is_displayed()
        assert self.browser.find_element(*self.planning_link).is_displayed()
        assert self.browser.find_element(*self.actuals_link).is_displayed()
        assert self.browser.find_element(*self.dashboard_link).is_displayed()
        assert self.browser.find_element(*self.users_link).is_displayed()
        assert self.browser.find_element(*self.projects_link).is_displayed()
        # assert self.browser.find_element(*self.help_menu).is_displayed()
        assert self.browser.find_element(*self.open_menu_button).is_displayed()

    def header_elements(self):
        wait = WebDriverWait(self.browser, 10)
        return self.browser.find_element(*self.header)

    def header_elements_text(self, number):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.header))
        elements = self.header_elements().find_elements(By.XPATH, "//a | //img | //button | //p")
         # Создаем список для хранения текстов элементов
        element_texts = []
    
    # Итерируемся по найденным элементам и добавляем их текст в список
        for element in elements:
            element_texts.append(element.text.strip())
    
    # Выводим тексты всех элементов в терминал
        for index, text in enumerate(element_texts):
            print(f"Element {index + 1}: {text}")
    
    # Возвращаем текст элемента с указанным номером (если необходимо)
        if number <= len(element_texts):
            return element_texts[number - 1]
        else:
            return ""
   
    def logout(self):
        wait = WebDriverWait(self.browser, 10)
        self.open_user_menu()
        logout = wait.until(EC.element_to_be_clickable(self.logout_button))
        logout.click()


class UserMenu:
    def __init__(self, browser, url):
        self.background = HeaderLocators.BACKGROUND
        self.browser = browser
        self.urls = url
        self.header = HeaderLocators.HEADER
        self.user_menu1 = HeaderLocators.USER_MENU
        self.organization_link = HeaderLocators.ORGANIZATION_LINK
        self.header_instance = Header(browser, url)
        self.profile_link = HeaderLocators.PROFILE_LINK
        self.my_week_link = HeaderLocators.MY_WEEK_LINK
        self.open_menu_button = HeaderLocators.OPEN_MENU_BUTTON

    def load(self):
        wait = WebDriverWait(self.browser, 10)
        self.browser.get(self.urls)
        wait.until(EC.presence_of_element_located(self.user_menu))

    def organization_link_open(self):
        wait = WebDriverWait(self.browser, 10)
        self.header_instance.open_user_menu()
        organization = wait.until(EC.element_to_be_clickable(self.organization_link))
        organization.click()
        time.sleep(3)

    def user_menu_links_count(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.user_menu1))
        links = self.browser.find_elements(*self.user_menu1)[0].find_elements(By.TAG_NAME, "a")
        return len(links)

    def user_menu_links(self):
        wait = WebDriverWait(self.browser, 10)
        user_menu = wait.until(EC.visibility_of_element_located(self.user_menu1))
        return user_menu.find_elements(By.TAG_NAME, "a") if user_menu else []

    def user_menu_link_text(self, number):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located(self.user_menu1))
        elements = self.browser.find_elements(*self.user_menu1)[0].find_elements(By.TAG_NAME, "a")
        return elements[number - 1].text

    def my_week_link_open(self):
        wait = WebDriverWait(self.browser, 10)
        self.header_instance.open_user_menu()
        my_week = wait.until(EC.element_to_be_clickable(self.my_week_link))
        my_week.click()
        wait.until(EC.url_contains("my-week"))

    def profile_link_open(self):
        wait = WebDriverWait(self.browser, 10)
        self.header_instance.open_user_menu()
        profile = wait.until(EC.element_to_be_clickable(self.profile_link))
        profile.click()
        wait.until(EC.url_contains("profile"))


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
        wait = WebDriverWait(self.browser, 10)
        self.browser.get(self.urls)
        wait.until(EC.presence_of_element_located(self.help_menu1))

    def help_menu_links(self):
        wait = WebDriverWait(self.browser, 10)
        elements = wait.until(EC.visibility_of_element_located(self.help_menu1)).find_elements(By.TAG_NAME, "a")
        return elements

    def help_menu_link_text(self):
        wait = WebDriverWait(self.browser, 10)
        help_menu = wait.until(EC.visibility_of_element_located(self.help_menu1))
        elements = help_menu.find_elements(By.TAG_NAME, "a") if help_menu else []
        text_list = [element.text.strip() for element in elements]
        return text_list

    def help_menu_links_count(self):
        wait = WebDriverWait(self.browser, 10)
        help_menu = wait.until(EC.visibility_of_element_located(self.help_menu1))
        elements = help_menu.find_elements(By.TAG_NAME, "a") if help_menu else []
        print(f"Number of elements in help menu: {len(elements)}")
        print(f"Elements: {elements}")
        return len(elements)
