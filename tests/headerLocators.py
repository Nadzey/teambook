from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGO = (By.CLASS_NAME, 'header-logo')
    OPEN_MENU_BUTTON = (By.ID, 'openUserMenu')
    LOGOUT_BUTTON = (By.XPATH, "//*[@id='header-menu']/div[3]/ul/li")
    ONBOARDING_HEADER = (By.CLASS_NAME, "onboarding__header")
    ORGANIZATION_LINK = (By.CSS_SELECTOR, '.tb__text__light-blue.col.menu__navlink.mobile_hidden:nth-child(3)')
    PROFILE_LINK = (By.CSS_SELECTOR, '.tb__text__light-blue.col.menu__navlink.mobile_hidden:first-child')
    MY_WEEK_LINK = (By.CSS_SELECTOR, '.tb__text__light-blue.col.menu__navlink.mobile_hidden:nth-child(2)')
    HELP = (By.CLASS_NAME, "mobile_hidden.header__help-icon-block")
    PLANNERS_LINK = (By.XPATH, "//a[normalize-space()='Planning']")
    DASHBOARD_LINK = (By.XPATH, "//a[normalize-space()='Dashboard']")
    USER_LINK = (By.XPATH, "//a[normalize-space()='Users']")
    PROJECT_LINK = (By.XPATH, "//a[normalize-space()='Projects']")
    HEADER_BLOCK = (By.CLASS_NAME, "header__items.mobile_hidden")
    ACTUALS_LINK = (By.PARTIAL_LINK_TEXT, 'Actuals')
    MUI_DIALOG_CLOSE = (By.CSS_SELECTOR, "[#':r6': > svg]")
    MUI_DIALOG = (By.CSS_SELECTOR, "[#':r6': > svg]")
    HEADER = (By.CSS_SELECTOR, '.row.header')
    USER_MENU = [By.XPATH, "//div[@id='header-menu']//ul[@role='menu']"]
    KNOWLEDGE_BASE_LINK = (By.XPATH,
                           "//div[@id='header-help-menu']//a[@class='tb__text__light-blue col menu__navlink']["
                           "normalize-space()='Knowledge Base']")
    CONTACT_US_LINK = (By.XPATH, "//a[normalize-space()='Contact Us']")
    SUGGEST_FEATURE_LINK = (By.XPATH, "//a[normalize-space()='Suggest a feature']")
    PRODUCT_ROAD_MAP_LINK = (By.XPATH, "//a[normalize-space()='Product Roadmap']")
    REOP_ONBOARD_LINK = (By.XPATH, "//a[normalize-space()='Reopen Onboarding']")
    REOP_DID_YOU_KNOW_LINK = (By.XPATH, "//div[@id='header-help-menu']//a[1]")
    HELP1 = [By.XPATH, "//div[@id='header-help-menu']//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded "
                       "MuiPaper-elevation1 MuiMenu-paper MuiPaper-root MuiPaper-elevation MuiPaper-rounded "
                       "MuiPaper-elevation8 MuiPopover-paper css-177ic5c']"]
    GETTING_STARTED = (By.CSS_SELECTOR, "onboarding__footer button")
    BACKGROUND = (By.CLASS_NAME, "MuiBackdrop-root MuiBackdrop-invisible MuiModal-backdrop css-esi9ax")
