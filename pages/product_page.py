from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_same_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text.strip()
        assert product_name == basket_product_name, f"Expected {product_name}, but got {basket_product_name}"

    def should_be_same_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text.strip()
        basket_total_alert = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_ALERT).text.strip()
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text.strip()
        assert price in basket_total_alert and price in basket_total, f"Expected {price}, but got {basket_total} in inner page and {basket_total_alert} in alert message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"