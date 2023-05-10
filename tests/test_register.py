from pages import register_page
from pages.planners_page import PlannersPage
from urls import PLANNERS_URL
from pages.settings_page import SettingsPage
import pytest


def test_create_organization(browser, login_page, reg_email, reg_password, first_name, last_name, company_name,
                             onboarding_header_text):
    email, password, first_name, last_name, company_name = reg_email, reg_password, first_name, last_name, company_name
    login_page.create_new_organization()
    register_page_instance = register_page.RegisterPage(browser)
    register_page_instance.fill_form(first_name, last_name, company_name, email, password)
    register_page_instance.accept_terms()
    register_page_instance.create_organization()
    register_page_instance.skip()

    assert "planners" in browser.current_url
    planners_page = PlannersPage(browser, PLANNERS_URL)
    planners_page.load()
    # assert planners_page.onboarding_header.text == onboarding_header_text

    planners_page.organization_link_open()
    settings_page = SettingsPage(browser)
    settings_page.load()
    settings_page.delete_company(company_name)
