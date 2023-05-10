from selenium.webdriver.common.by import By


class SettingsPageLocators:
    DELETE_ORGANIZATION_P = (By.XPATH, "//p[normalize-space()='Delete Organization']")
    DELETE_BUTTON = (By.ID, 'deleteAccountButton')
    COMPANY_NAME_INPUT = (By.ID, 'name')
    DELETE_ACCOUNT_BUTTON = (By.ID, 'deleteAccount')
