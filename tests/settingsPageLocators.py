from selenium.webdriver.common.by import By


class SettingsPageLocators:
    DELETE_ORGANIZATION_P = (By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[1]/div/div[7]/p')
    DELETE_BUTTON = (By.ID, 'delete-account-button')
    COMPANY_NAME_INPUT = (By.ID, 'name')
    DELETE_ACCOUNT_BUTTON = (By.ID, 'delete-account')
