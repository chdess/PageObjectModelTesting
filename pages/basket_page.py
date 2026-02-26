from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_text_about_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "There is no text that says the basket is empty"