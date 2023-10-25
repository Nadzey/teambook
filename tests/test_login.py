from urls import PLANNERS_URL, LOGIN_URL
from pages.header import Header
import pytest
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()
VALID_EMAIL = os.environ["VALID_EMAIL"]
VALID_PASSWORD = os.environ["VALID_PASSWORD"]

def test_valid_login(browser, login_page):
    # Preconditions
   
    # Steps
    # login_page = LoginPage(browser, LOGIN_URL)
    # login_page.load()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)
    # Expected result
    assert "planners" in browser.current_url
    # logout
    header = Header(browser, PLANNERS_URL)
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
    password = VALID_PASSWORD
    # Steps
    login_page.login(email, password)
    # Expected result
    assert login_page.get_error_message() == error_message


@pytest.mark.parametrize("password", [""])
def test_blank_password_login(browser, login_page, error_message, password, valid_email):
    # Preconditions
    email = VALID_EMAIL
    # Steps
    login_page.login(email, password)
    # Expected result
    assert login_page.get_error_message() == error_message