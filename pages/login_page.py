from .base_page import Base_page
from .locators import Login_page_locators

link = 'https://www.saucedemo.com/'
standard_name = "standard_user"
locked_name = "locked_out_user"
correct_password = "secret_sauce"
not_correct_password = "not_secret_sauce"


class Login_page(Base_page):
    def open_login_page(self):
        self.open_url()
        self.assert_current_page(link)

    def login_correct_user(self):
        self.input_text(*Login_page_locators.user_name, standard_name)

    def login_locked_user(self):
        self.input_text(*Login_page_locators.user_name, locked_name)

    def enter_password(self):
        self.input_text(*Login_page_locators.password, correct_password)

    def enter_not_correct_password(self):
        self.input_text(*Login_page_locators.password, not_correct_password)

    def click_login_button(self):
        self.click_element(*Login_page_locators.login_button)

    def get_error_text(self):
        element = self.driver.find_element(*Login_page_locators.error_text)
        return element.text
