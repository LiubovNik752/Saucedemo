from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import Base


class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    main_word = "//div[@class='app_logo']"
    locked_word = "//h3[@data-test='error']"


    # Variables

    correct_name = "standard_user"
    locked_name = "locked_out_user"
    correct_password = "secret_sauce"


    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_locked_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locked_word)))


    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")


    # Methods

    def authorization_positive(self):

        self.input_user_name(self.correct_name)
        self.input_password(self.correct_password)
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Swag Labs")

    def authorization_negative(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.input_user_name(self.locked_name)
        self.input_password(self.correct_password)
        self.click_login_button()
        self.assert_word(self.get_locked_word(), "Epic sadface: Sorry, this user has been locked out.")