import time
import pytest
from pages.login_page import Login_page
from pages.main_page import Main_page


class Test_login_page:
    link = 'https://www.saucedemo.com/'
    base_page_url = "https://www.saucedemo.com/inventory.html"

    @pytest.mark.smoke
    def test_correct_authorization(self, driver):
        page = Login_page(driver, self.link)
        page.open_login_page()
        page.login_correct_user()
        page.enter_password()
        page.click_login_button()
        page.assert_current_page(self.base_page_url)

    @pytest.mark.smoke
    def test_unauthorization(self, check_in):
        page = Main_page(check_in, self.link)
        page.click_burger_menu_button()
        time.sleep(2)
        page.click_logout_button()
        time.sleep(2)
        assert check_in.current_url == "https://www.saucedemo.com/"

    @pytest.mark.extra
    def test_authorization_logout_user(self, driver):
        page = Login_page(driver, self.link)
        page.open_login_page()
        page.login_locked_user()
        page.enter_password()
        page.click_login_button()
        error_text = page.get_error_text()
        assert error_text == "Epic sadface: Sorry, this user has been locked out."

    @pytest.mark.extra
    def test_authorization_wrong_password(self, driver):
        page = Login_page(driver, self.link)
        page.open_login_page()
        page.login_correct_user()
        page.enter_not_correct_password()
        page.click_login_button()
        error_text = page.get_error_text()
        assert error_text == "Epic sadface: Username and password do not match any user in this service"

    @pytest.mark.extra
    def test_authorization_wrong_username(self, driver):
        page = Login_page(driver, self.link)
        page.open_login_page()
        page.login_not_correct_username()
        page.enter_password()
        page.click_login_button()
        error_text = page.get_error_text()
        assert error_text == "Epic sadface: Username and password do not match any user in this service"
