from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, "//input[@id=':r3:']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id=':r4:']")
    REG_EMAIL_INPUT = (By.XPATH, "//input[@id=':r5:']")
    COMPANY_NAME_INPUT = (By.XPATH, "//input[@id=':r6:']")
    REG_PASSWORD_INPUT = (By.ID, 'password_field')
    AGREE_CHECKBOX = (By.ID, 'marketing-accept-checkbox')
    CREATE_ORGANIZATION_BUTTON = (By.ID, 'create-account')
    SKIP_P = (By.XPATH, "//p[normalize-space()='Skip']")
