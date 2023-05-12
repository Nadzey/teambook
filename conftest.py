import pytest
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from urls import LOGIN_URL, PLANNERS_URL


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


@pytest.fixture(scope="function")
def header(browser):
    page = header(browser, PLANNERS_URL)
    page.load()
    return page


@pytest.fixture
def error_message():
    return "Wrong email or password!"


@pytest.fixture
def error_message1():
    return "An account with this email address already exist. Please use another Email OR login to existing one."


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


@pytest.fixture
def registration_data():
    return {
        "email": "test@example.com",
        "password": "Test123!",
        "first_name": "John",
        "last_name": "Doe",
        "company_name": "Test test Company",
    }


@pytest.fixture
def onboarding_header_text():
    return "GETTING STARTED IN TEAMBOOK"


@pytest.fixture
def planning_text():
    return "Planning"


@pytest.fixture
def actuals_text():
    return "Actuals"


@pytest.fixture
def dashboard_text():
    return "Dashboard"


@pytest.fixture
def users_text():
    return "Users"


@pytest.fixture
def projects_text():
    return "Projects"


@pytest.fixture
def user_menu_text():
    return "Test"


@pytest.fixture
def profile_text():
    return "Profile"


@pytest.fixture
def my_week_text():
    return "My Week"


@pytest.fixture
def organization_text():
    return "Organization"
