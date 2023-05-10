import pytest
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from urls import LOGIN_URL


@pytest.fixture(scope="session")
def browser():
    service = Service('./chromedriver.exe')
    driver = Chrome(service=service)
    driver.maximize_window()
    screenshot_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "result")
    screenshot_num = 0
    yield driver
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    while os.path.exists(os.path.join(screenshot_dir, f"screenshot_{screenshot_num}.png")):
        screenshot_num += 1
    screenshot_name = f"screenshot_{screenshot_num}.png"
    driver.save_screenshot(os.path.join(screenshot_dir, screenshot_name))
    driver.quit()


@pytest.fixture(scope="session")
def urls():
    urls_path = os.path.join(os.path.dirname(__file__), "urls.py")
    with open(urls_path) as f:
        urls = [line.strip() for line in f if line.strip()]
    return urls


@pytest.fixture(scope="function")
def login_page(browser):
    page = LoginPage(browser, LOGIN_URL)
    page.load()
    return page


@pytest.fixture
def error_message():
    return "Wrong email or password!"


@pytest.fixture(params=[
    ("teambooktestgmail.com", "Test123!")
])
def invalid_email(request):
    return request.param


@pytest.fixture(params=[
    ("teambooktest@gmail.com", "Test321!")
])
def invalid_password(request):
    return request.param


@pytest.fixture(params=["teambooktest@gmail.com"])
def valid_email(request):
    return request.param


@pytest.fixture(params=["Test123!"])
def valid_password(request):
    return request.param


@pytest.fixture(params=["teambooktest1@gmail.com"])
def reg_email(request):
    return request.param


@pytest.fixture(params=["Test123!"])
def reg_password(request):
    return request.param


@pytest.fixture(params=["John"])
def first_name(request):
    return request.param


@pytest.fixture(params=["Snow"])
def last_name(request):
    return request.param


@pytest.fixture(params=["NewTest LLC"])
def company_name(request):
    return request.param


@pytest.fixture
def onboarding_header_text():
    return "GETTING STARTED IN TEAMBOOK"
