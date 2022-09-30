from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    BASKET_COST = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-hs")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.allertinner")