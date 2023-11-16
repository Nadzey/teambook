from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRST_NAME_INPUT = (By.ID, "register-first-name")
    LAST_NAME_INPUT = (By.ID, "register-last-name")
    REG_EMAIL_INPUT = (By.ID, "register-email")
    COMPANY_NAME_INPUT = (By.ID, "register-company-name")
    REG_PASSWORD_INPUT = (By.ID, 'password-field')
    AGREE_CHECKBOX = (By.CSS_SELECTOR, '[aria-label="not checked"]')
    CREATE_ORGANIZATION_BUTTON = (By.ID, 'create_org_btn')
    SKIP_P = (By.CSS_SELECTOR, 'div.MuiDialogActions-root.MuiDialogActions-spacing > p')
    ERROR_MESSAGE = (By.XPATH, "//p[@class='form-error__error-text']")
