from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Item in basket"

    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"

    def guest_can_go_to_basket_page(self):
        button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        button.click()