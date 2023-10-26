import pytest
import os
from selenium.webdriver import Chrome
from pages.login_page import LoginPage
from urls import LOGIN_URL
import time
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from _pytest.config import ExitCode


@pytest.fixture(scope="session")
def browser(request):
    chromedriver_autoinstaller.install() 

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=3') 
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--enable-javascript')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    
    if request.config.getoption("--headed"):
        chrome_options.add_argument('--disable-extensions')
    else:
        chrome_options.add_argument('--headless')

    driver = Chrome(options=chrome_options)
    driver.maximize_window()
    
    take_screenshot_on_failure = False
    screenshot_dir = "" 
    screenshot_num = 0

    def finalize():
        nonlocal take_screenshot_on_failure
        nonlocal screenshot_dir
        nonlocal screenshot_num
        if take_screenshot_on_failure:
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            for filename in os.listdir(screenshot_dir):
                if filename.startswith("screenshot_") and filename.endswith(".png"):
                    os.remove(os.path.join(screenshot_dir, filename))
            while os.path.exists(os.path.join(screenshot_dir, f"screenshot_{screenshot_num}.png")):
                screenshot_num += 1
            screenshot_name = f"screenshot_{screenshot_num}.png"
            driver.save_screenshot(os.path.join(screenshot_dir, screenshot_name))
        driver.quit()

    request.addfinalizer(finalize)
    yield driver

def pytest_exception_interact(node, call, report):
    global take_screenshot_on_failure
    if report.failed:
        take_screenshot_on_failure = True
    return None


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Run tests in headed mode")


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


@pytest.fixture(autouse=False)
def logout_after_test(request):
    yield
    # After each test, perform the logout operation
    request.node.cls.logout()
    time.sleep(3)


@pytest.fixture
def authenticated_user(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login(valid_email, valid_password)
    yield


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
        "company_name": "Test test Company1",
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
    return "John\nJS"


@pytest.fixture
def profile_text():
    return "Profile"


@pytest.fixture
def my_week_text():
    return "My Week"


@pytest.fixture
def organization_text():
    return "Organization"


@pytest.fixture
def knowledge_text():
    return 'Knowledge Base'


@pytest.fixture
def contact_us_text():
    return "Contact Us"


@pytest.fixture
def roadmap_text():
    return "Product Roadmap"


@pytest.fixture
def suggest_feature_text():
    return "Suggest a feature"
