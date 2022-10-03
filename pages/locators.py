from selenium.webdriver.common.by import By

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_IN_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_IN_FORM1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_IN_FORM2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[value = 'Register']")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_COST_IN_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-hs")
    PRODUCT_COST = (By.CSS_SELECTOR, "p.price-color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "strong")
    PRODUCT_NAME_MESSAGE = (By.TAG_NAME, "h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    BASKET_COST = (By.CSS_SELECTOR, ".alertinner :nth-child(1) strong")
    
class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default:first-child")
    BASKET_MESSAGE = (By.ID, "content_inner")
    PRODUCT_IN_BASKET = (By.CLASS_NAME, "basket-items")
    