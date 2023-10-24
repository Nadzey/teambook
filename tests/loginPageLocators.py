from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@id=':r0:']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id=':r1:']")
    LOGIN_BUTTON = (By.ID, "login_btn")
    ERROR_MESSAGE = (By.XPATH, "//p[@class='form-error__error-text']")
    CREATE_ORGANIZATION_LINK = (By.LINK_TEXT, 'Or create new Organization')
