import time
import pytest
from selenium import webdriver
from pages.login_page import Login_page, link


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    time.sleep(3)

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def check_in():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    page = Login_page(driver, link)
    page.open_login_page()
    page.login_correct_user()
    page.enter_password()
    page.click_login_button()
    time.sleep(3)

    yield driver

    driver.quit()
