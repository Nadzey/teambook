from pages.header import UserMenu
from urls import PLANNERS_URL
from pages.settings_page import SettingsPage


def test_delete_organization(browser, login_page, registration_data):
    # precondition
    email, password = registration_data["email"], registration_data["password"]
    login_page.login(email, password)

    user_menu = UserMenu(browser, PLANNERS_URL)
    user_menu.load()
    user_menu.organization_link_open()
    # Steps
    settings_page = SettingsPage(browser)
    settings_page.load()
    settings_page.delete_company(registration_data["company_name"])
    # Expected result
    assert "register" in browser.current_url.lower()
