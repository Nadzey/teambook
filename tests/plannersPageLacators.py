from selenium.webdriver.common.by import By


class plannersPageLocators:
    LOGO = (By.CLASS_NAME, 'header-logo')
    OPEN_MENU_BUTTON = (By.ID, 'openUserMenu')
    LOGOUT_BUTTON = (By.XPATH, "//li[@role='menuitem']")
