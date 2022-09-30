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
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        WebDriverWait(self.browser, 2).until(EC.alert_is_present())
        #time.sleep(1)
        alert.accept()
        #time.sleep(2)
        #WebDriverWait(self.browser, 2).until(EC.alert_is_present())
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            WebDriverWait(self.browser, 2).until(EC.alert_is_present())
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        
    def should_be_cost_basket(self):
        # реализуйте проверку, что есть форма логина
        cost = self.browser.find_element(*ProductPageLocators.BASKET_COST)
        assert cost == "9,99", "There is no basket cost"
        
    def should_be_name_match(self):
        text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert "The shellcoder's handbook был добавлен в вашу корзину." == text, "PRODUCT_NAME is false"

