from pages.login_page import LoginPage
from urls import LOGIN_URL, PLANNERS_URL
from pages.planners_page import PlannersPage


def test_valid_login(browser, valid_credentials):
    # Preconditions
    email, password = valid_credentials
    login_page = LoginPage(browser, LOGIN_URL)
    login_page.load()

    # Steps
    login_page.login(email, password)

    # Expected result
    assert browser.current_url == PLANNERS_URL
    planners_page = PlannersPage(browser, PLANNERS_URL)
    planners_page.load()
    assert planners_page.is_header_logo_displayed()

    # logout
    planners_page.logout()

def test_invalid_email_login(browser, invalid_email_credentials, error_message):
    # Preconditions
    email, password = invalid_email_credentials
    login_page = LoginPage(browser, LOGIN_URL)
    login_page.load()

    # Steps
    login_page.login(email, password)

    assert login_page.get_error_message() == error_message


def test_invalid_password_login(browser, invalid_password_credentials, error_message):
    # Preconditions
    email, password = invalid_password_credentials
    login_page = LoginPage(browser, LOGIN_URL)
    login_page.load()

    # Steps
    login_page.login(email, password)

    assert login_page.get_error_message() == error_message
