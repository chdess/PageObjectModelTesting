from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")

class LoginPageLocators():
    REG_FORM = (By.XPATH, "//form[@id='register_form']")
    REG_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REG_PASS = (By.XPATH, "//input[@id='id_registration-password1']")
    REG_PASS_CON = (By.XPATH, "//input[@id='id_registration-password2']")
    AUTH_FORM = (By.XPATH, "//form[@id='login_form']")
    AUTH_EMAIL = (By.XPATH, "//input[@id='id_login-username']")
    AUTH_PASS = (By.XPATH, "//input[@id='id_login-password']")
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")
    PRICE = (By.XPATH, "//p[contains(@class,'price_color')]")
    BASKET_TOTAL = (By.XPATH, "//div[contains(@class, 'basket')]")
    BASKET_ALERT = (By.XPATH, "//div[contains(@class, 'alertinner') and not (contains(text(), 'basket')) and not(p)]")
    BASKET_PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'alertinner') and not (contains(text(), 'basket')) and not(p)]/strong")
    BASKET_TOTAL_ALERT = (By.XPATH, "//div[contains(@class, 'alertinner') and not (contains(text(), 'basket'))]/p/strong")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
