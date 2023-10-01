import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import Main_page
from pages.login_page import Login_page


def test_correct_authorization(set_up):
    driver = webdriver.Chrome()
    login = Login_page(driver)
    login.authorization_positive()
    print("Successfully authorization")

    # enter_shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="shopping_cart_link"]')))
    # enter_shopping_cart.click()
    # print("Click enter shopping cart")

@pytest.mark.skip
def test_incorrect_authorization(set_up):
    driver = webdriver.Chrome()
    login = Login_page(driver)
    login.authorization_negative()
    print("Impossible authorise with locked name")

# @pytest.mark.skip
# def test_logout():


def test_buy_product(set_up):
    driver = webdriver.Chrome()
    mp = Main_page(driver)
    mp.select_product_backpack()