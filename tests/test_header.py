from urls import PROJECT_URL, PLANNERS_URL, USER_URL, ACTUALS_URL, DASHBOARD_URL, PROFILE_URL, SETTINGS_SETTINGS_URL
from pages.header import Header, UserMenu, HelpMenu


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

    assert "planners" in browser.current_url


def test_elements_present_in_header(browser, planning_text, actuals_text, dashboard_text, users_text, projects_text,
                                    user_menu_text):
    # steps
    header = Header(browser, PLANNERS_URL)
    header.verify_elements_present()
    # Expected result
    assert header.header_elements_text(3) == planning_text
    assert header.header_elements_text(4) == actuals_text
    assert header.header_elements_text(5) == dashboard_text
    assert header.header_elements_text(6) == users_text
    assert header.header_elements_text(7) == projects_text
    assert header.header_elements_text(9) == user_menu_text


def test_user_menu_links_present(browser, profile_text, my_week_text, organization_text):
    # steps
    header_instance = Header(browser, PLANNERS_URL)
    user_menu_instance = UserMenu(browser, PLANNERS_URL)
    header_instance.load()
    header_instance.open_user_menu()
    # Expected result
    assert user_menu_instance.user_menu_links_count() == 4
    assert user_menu_instance.user_menu_link_text(1) == profile_text
    assert user_menu_instance.user_menu_link_text(2) == my_week_text
    assert user_menu_instance.user_menu_link_text(3) == organization_text


def test_my_week_link_transfer_user_to_correct_URL(browser):
    user_menu = UserMenu(browser, PLANNERS_URL)
    user_menu.load()
    user_menu.my_week_link_open()
    assert "my-week" in browser.current_url


def test_profile_link_transfer_user_to_correct_URL(browser):
    user_menu = UserMenu(browser, PLANNERS_URL)
    user_menu.load()
    user_menu.profile_link_open()
    assert browser.current_url == PROFILE_URL


def test_organization_link_transfer_user_to_correct_URL(browser):
    user_menu = UserMenu(browser, PLANNERS_URL)
    user_menu.load()
    user_menu.organization_link_open()
    assert browser.current_url == SETTINGS_SETTINGS_URL


def test_help_menu_links_present(browser, knowledge_text, contact_us_text, roadmap_text, suggest_feature_text):
    # steps
    help_menu = HelpMenu(browser, PLANNERS_URL)
    help_menu.load()
    help_menu.click_help_menu()
    # Expected result
    assert help_menu.help_menu_links_count() == 6
    assert help_menu.help_menu_link_text(1) == knowledge_text
    assert help_menu.help_menu_link_text(2) == contact_us_text
    assert help_menu.help_menu_link_text(3) == suggest_feature_text
    assert help_menu.help_menu_link_text(4) == roadmap_text


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


def test_clicking_on_logo_return_to_planner_page(browser):
    # steps
    header_instance = Header(browser, PLANNERS_URL)
    user_menu_instance = UserMenu(browser, PLANNERS_URL)
    header_instance.load()
    header_instance.click_on_header_logo()
    # Expected result
    assert "planners" in browser.current_url

    # logout
    user_menu_instance.load()
    user_menu_instance.logout()
