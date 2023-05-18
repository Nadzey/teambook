from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGO = (By.CLASS_NAME, 'header-logo')
    OPEN_MENU_BUTTON = [By.ID, 'openUserMenu']
    LOGOUT_BUTTON = (By.XPATH, "//li[@role='menuitem']")
    ONBOARDING_HEADER = (By.CLASS_NAME, "onboarding__header")
    ORGANIZATION_LINK = (By.XPATH, "//a[normalize-space()='Organization']")
    PROFILE_LINK = (By.XPATH, "//a[normalize-space()='Profile']")
    MY_WEEK_LINK = (By.XPATH, "//a[normalize-space()='My Week']")
    HELP = (By.XPATH, "//div[@class='mobile_hidden header__help-icon-block']")
    PLANNERS_LINK = (By.XPATH, "//a[normalize-space()='Planning']")
    DASHBOARD_LINK = (By.XPATH, "//a[normalize-space()='Dashboard']")
    USER_LINK = (By.XPATH, "//a[normalize-space()='Users']")
    PROJECT_LINK = (By.XPATH, "//a[normalize-space()='Projects']")
    HEADER_BLOCK = (By.CLASS_NAME, "header__items.mobile_hidden")
    ACTUALS_LINK = (By.CSS_SELECTOR, "a[href='/actuals")
    MUI_DIALOG_CLOSE = (By.CSS_SELECTOR, "svg.MuiSvgIcon-root")
    MUI_DIALOG = (By.CSS_SELECTOR,
                  "body > div.MuiModal-root.MuiDialog-root.tb-default-dialog.css-126xj0f > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div")
    HEADER = (By.CSS_SELECTOR, '.row.header')
    USER_MENU = [By.XPATH, "//div[@id='header-menu']//ul[@role='menu']"]
    KNOWLEDGE_BASE_LINK = (By.XPATH,
                           "//div[@id='header-help-menu']//a[@class='tb__text__light-blue col menu__navlink'][normalize-space()='Knowledge Base']")
    CONTACT_US_LINK = (By.XPATH, "//a[normalize-space()='Contact Us']")
    SUGGEST_FEATURE_LINK = (By.XPATH, "//a[normalize-space()='Suggest a feature']")
    PRODUCT_ROAD_MAP_LINK = (By.XPATH, "//a[normalize-space()='Product Roadmap']")
    REOP_ONBOARD_LINK = (By.XPATH, "//a[normalize-space()='Reopen Onboarding']")
    REOP_DID_YOU_KNOW_LINK = (By.XPATH, "//div[@id='header-help-menu']//a[1]")
