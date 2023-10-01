import pytest
from selenium import webdriver

from pages.login_page import Login_page


@pytest.fixture()
def set_up():
    driver = webdriver.Chrome()

    url = 'https://www.saucedemo.com/'
    driver.get(url)
    driver.maximize_window()

    yield set_up

    driver.quit()