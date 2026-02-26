from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_LINK = (By.XPATH, "//a[contains(@href, 'basket/') and not(contains(@class,'navbar-right'))]")
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    LOGIN_LINK_INVALID = (By.XPATH, "//a[@id='login_link_inc']")
    USER_ICON = (By.XPATH, "//*[@class='icon-user']")


class BasketPageLocators():
    BASKET_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")
    BASKET_ITEMS = (By.XPATH, "//div[@id='basket-items']")

#class MainPageLocators():



class LoginPageLocators():
    AUTH_EMAIL = (By.XPATH, "//input[@id='id_login-username']")
    AUTH_FORM = (By.XPATH, "//form[@id='login_form']")
    AUTH_PASS = (By.XPATH, "//input[@id='id_login-password']")
    REG_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REG_FORM = (By.XPATH, "//form[@id='register_form']")
    REG_PASS = (By.XPATH, "//input[@id='id_registration-password1']")
    REG_PASS_CON = (By.XPATH, "//input[@id='id_registration-password2']")
    REG_SUBMIT = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")
    BASKET_ALERT = (By.XPATH, "//div[contains(@class, 'alertinner') and not (contains(text(), 'basket')) and not(p)]")
    BASKET_PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'alertinner') and not (contains(text(), 'basket')) and not(p)]/strong")
    BASKET_TOTAL = (By.XPATH, "//div[contains(@class, 'basket')]")
    BASKET_TOTAL_ALERT = (By.XPATH, "//div[contains(@class, 'alertinner') and not (contains(text(), 'basket'))]/p/strong")
    PRICE = (By.XPATH, "//p[contains(@class,'price_color')]")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]")
