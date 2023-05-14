from urls import PLANNERS_URL
from pages.header import Header
import pytest


def test_valid_login(browser, valid_email, valid_password, login_page, urls):
    # Preconditions
    email, password = valid_email, valid_password
    # Steps
    login_page.login(email, password)
    # Expected result
    assert browser.current_url == PLANNERS_URL
    header = Header(browser, PLANNERS_URL)
    header.load()

    # logout
    header.logout()


def test_invalid_email_login(browser, invalid_email, login_page, error_message):
    # Preconditions
    email, password = invalid_email
    # Steps
    login_page.login(email, password)
    # Expected result
    assert login_page.get_error_message() == error_message


def test_invalid_password_login(browser, invalid_password, login_page, error_message):
    # Preconditions
    email, password = invalid_password
    # Steps
    login_page.login(email, password)
    # Expected result
    assert login_page.get_error_message() == error_message


@pytest.mark.parametrize("email, password", [("", "")])
def test_blank_emailPassword_login(browser, login_page, error_message, email, password):
    # Steps
    login_page.login(email, password)
    # Expected result
    assert login_page.get_error_message() == error_message


@pytest.mark.parametrize("email", [""])
def test_blank_email_login(browser, login_page, error_message, email, valid_password):
    # Preconditions
    password = valid_password
    # Steps
    login_page.login(email, password)
    # Expected result
    assert login_page.get_error_message() == error_message


@pytest.mark.parametrize("password", [""])
def test_blank_password_login(browser, login_page, error_message, password, valid_email):
    # Preconditions
    email = valid_email
    # Steps
    login_page.login(email, password)
    # Expected result
    assert login_page.get_error_message() == error_message
