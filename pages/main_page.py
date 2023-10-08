from pages.base_page import Base_page
from .locators import Main_page_locators, Cart_page_locators
from selenium.webdriver.support.ui import Select


class Main_page(Base_page):
    def click_burger_menu_button(self):
        self.click_element(*Main_page_locators.burger_menu_button)

    def click_logout_button(self):
        self.click_element(*Main_page_locators.logout_button)

    def click_product_backpack(self):
        self.click_element(*Main_page_locators.backpack_btn)

    def click_product_bike_light(self):
        self.click_element(*Main_page_locators.bike_light_btn)

    def click_product_tshirt_black(self):
        self.click_element(*Main_page_locators.tshirt_black_btn)

    def click_product_fleece_jacket(self):
        self.click_element(*Main_page_locators.fleece_jacket_btn)

    def click_product_onesie(self):
        self.click_element(*Main_page_locators.onesie_btn)

    def click_product_tshirt_red(self):
        self.click_element(*Main_page_locators.tshirt_red_btn)

    def get_product_name_backpack(self):
        element = self.driver.find_element(*Main_page_locators.product_name_backpack)
        return element.text

    def get_product_name_bike_light(self):
        element = self.driver.find_element(*Main_page_locators.product_name_bike_light)
        return element.text

    def get_product_name_tshirt_black(self):
        element = self.driver.find_element(*Main_page_locators.product_name_tshirt_black)
        return element.text

    def get_product_name_fleece_jacket(self):
        element = self.driver.find_element(*Main_page_locators.product_name_fleece_jacket)
        return element.text

    def get_product_name_onesie(self):
        element = self.driver.find_element(*Main_page_locators.product_name_onesie)
        return element.text

    def get_product_name_tshirt_red(self):
        element = self.driver.find_element(*Main_page_locators.product_name_tshirt_red)
        return element.text

    def get_cart_product_name(self):
        element = self.driver.find_element(*Cart_page_locators.product_name)
        return element.text

    def get_cart_counter(self):
        element = self.driver.find_element(*Main_page_locators.cart_counter)
        return element.text

    def click_cart_icon(self):
        self.click_element(*Main_page_locators.cart_icon)

    def click_sort_btn(self):
        self.click_element(*Main_page_locators.sort_btn)

    def get_list_price(self):
        lst = self.driver.find_elements(*Main_page_locators.product_price)
        price_lst = []
        for i in lst:
            price_lst.append(float(i.text.lstrip('$')))
        return price_lst

    def get_list_names(self):
        lst = self.driver.find_elements(*Main_page_locators.product_name)
        name_lst = []
        for i in lst:
            name_lst.append(i.text)
        return name_lst

    def click_sort_price_lohi(self):
        select = Select(self.driver.find_element(*Main_page_locators.select))
        select.select_by_value("lohi")

    def click_sort_price_hilo(self):
        select = Select(self.driver.find_element(*Main_page_locators.select))
        select.select_by_value("hilo")

    def click_sort_name_az(self):
        select = Select(self.driver.find_element(*Main_page_locators.select))
        select.select_by_value("az")
