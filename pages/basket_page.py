from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Basket is not empty"

    def should_be_message_basket(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE)
        assert "Your basket is empty" in basket_message.text, "No message about basket empty"