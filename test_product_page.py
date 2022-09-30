from .pages.product_page import ProductPage
from selenium import webdriver
import pytest
import time

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code():
        page.should_be_name_match()
        page.should_be_cost_basket()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_message_basket()
    page.should_not_be_products_in_basket()
    

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()
    
    
class TestUserAddToBasketFromProductPage(): 
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakeemail.com"
        password = "987654321"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    
    @pytest.mark.need_review   
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_name_match()
        page.should_be_cost_basket()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()