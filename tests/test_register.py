from pages import register_page
from pages.header import UserMenu
from urls import PLANNERS_URL


def test_create_organization(browser, login_page, registration_data):
    # Steps
    login_page.create_new_organization()
    register_page_instance = register_page.RegisterPage(browser)
    register_page_instance.fill_form(**registration_data)
    register_page_instance.accept_terms()
    register_page_instance.create_organization()
    register_page_instance.skip()
    # Expected result
    assert "planners" in browser.current_url
    # logout
    user_menu = UserMenu(browser, PLANNERS_URL)
    user_menu.logout()


def test_create_organization_with_existing_data(browser, login_page, registration_data, error_message1):
    # Steps
    login_page.create_new_organization()
    register_page_instance = register_page.RegisterPage(browser)
    register_page_instance.fill_form(**registration_data)
    register_page_instance.accept_terms()
    register_page_instance.create_organization()
    # Expected result
    assert "planners" not in browser.current_url

    assert register_page_instance.get_error_message() == error_message1