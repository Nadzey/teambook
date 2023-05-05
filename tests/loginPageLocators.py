from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@id=':r0:']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id=':r1:']")
    LOGIN_BUTTON = (By.ID, "login-button")