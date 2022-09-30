from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time 

class ProductPage(BasePage): 
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        
    def should_be_cost_basket(self):
        # реализуйте проверку, что есть форма логина
        cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        assert cost == "9,99", "There is no basket cost"
        
    def should_be_name_match(self):
        text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert "The shellcoder's handbook был добавлен в вашу корзину." == text, "PRODUCT_NAME is false"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Should not be success message"
        
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message do not disappear"

