from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import math
import time 

class ProductPage(BasePage): 
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        
    def should_be_cost_basket(self):
        cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        cost_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_IN_BASKET)
        assert cost == cost_in_basket, \
            "There is no basket cost"
        
    def should_be_name_match(self):
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert message == product_name, \
            "PRODUCT_NAME is false"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but it is not"  

