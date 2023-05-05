import pytest
import time
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    service = Service('./chromedriver.exe')
    driver = Chrome(service=service)
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

@pytest.fixture
def valid_credentials():
    return "teambooktest@gmail.com", "Test123!"

@pytest.fixture(scope="session")
def urls():
    urls_path = os.path.join(os.path.dirname(__file__), "urls.py")
    with open(urls_path) as f:
        urls = [line.strip() for line in f if line.strip()]
    return urls
