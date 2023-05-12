from urls import PROJECT_URL, PLANNERS_URL, USER_URL, ACTUALS_URL, DASHBOARD_URL
from pages.header import Header


def test_header_block_links(browser, valid_email, valid_password, login_page, urls, planning_text, actuals_text,
                            dashboard_text, users_text, projects_text):
    # Preconditions
    email, password = valid_email, valid_password
    login_page.login(email, password)
    # steps
    header = Header(browser, PLANNERS_URL)
    # Expected result
    assert header.header_block_links_count() == 5
    assert header.header_block_link_text(1) == planning_text
    assert header.header_block_link_text(2) == actuals_text
    assert header.header_block_link_text(3) == dashboard_text
    assert header.header_block_link_text(4) == users_text
    assert header.header_block_link_text(5) == projects_text

    assert browser.current_url == PLANNERS_URL


def test_elements_present(browser, planning_text, actuals_text, dashboard_text, users_text, projects_text,
                          user_menu_text):
    # steps
    header = Header(browser, PLANNERS_URL)
    header.verify_elements_present()
    # Expected result
    assert header.header_elements_text(1) == planning_text
    assert header.header_elements_text(2) == actuals_text
    assert header.header_elements_text(3) == dashboard_text
    assert header.header_elements_text(4) == users_text
    assert header.header_elements_text(5) == projects_text
    assert header.header_elements_text(6) == user_menu_text


def test_project_link_opens(browser):
    # steps
    header = Header(browser, PROJECT_URL)
    header.load()
    header.click_projects_link()
    # Expected result
    assert browser.current_url == PROJECT_URL


def test_users_link_opens(browser):
    # steps
    header = Header(browser, USER_URL)
    header.load()
    header.click_users_link()
    # Expected result
    assert browser.current_url == USER_URL


def test_dashboard_link_opens(browser):
    # steps
    header = Header(browser, DASHBOARD_URL)
    header.load()
    header.click_dashboard_link()
    # Expected result
    assert browser.current_url == DASHBOARD_URL


def test_actuals_link_opens(browser):
    # steps
    header = Header(browser, ACTUALS_URL)
    header.load()
    header.click_actuals_link()
    # Expected result
    assert browser.current_url == ACTUALS_URL


def test_user_menu_links_present(browser, profile_text, my_week_text, organization_text):
    # steps
    header = Header(browser, PLANNERS_URL)
    header.load()
    header.open_user_menu()
    # Expected result
    assert header.user_menu_links_count() == 3
    assert header.user_menu_link_text(1) == profile_text
    assert header.user_menu_link_text(2) == my_week_text
    assert header.user_menu_link_text(3) == organization_text


def test_clicking_on_logo_return_to_planner_page(browser):
    # steps
    header = Header(browser, PLANNERS_URL)
    # header.load()
    header.click_on_header_logo()
    # Expected result
    assert "planners" in browser.current_url

    # logout
    header.logout()
