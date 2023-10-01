from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    select_product_backpack = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_bike_light = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_Tshirt = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    select_product_jacket = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    select_product_onesie = "//button[@id='add-to-cart-sauce-labs-onesie']"
    select_product_Tshirt_red = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    cart = "//div[@id='shopping_cart_container']"


    # Variables


    # Getters

    def get_product_backpack(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_backpack)))

    def get_product_bike_light(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_bike_light)))

    def get_product_Tshirt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_Tshirt)))

    def get_product_jacket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_jacket)))

    def get_product_onesie(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_onesie)))

    def get_product_Tshirt_red(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_Tshirt_red)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    # Actions

    def click_product_backpack(self):
        self.get_product_backpack().click()
        print("Click product backpack")

    def click_product_bike_light(self):
        self.get_product_bike_light().click()
        print("Click product bike light")

    def click_product_Tshirt(self):
        self.get_product_Tshirt().click()
        print("Click product T-shirt")

    def click_product_jacket(self):
        self.get_product_jacket().click()
        print("Click product jacket")

    def click_product_onesie(self):
        self.get_product_onesie().click()
        print("Click product Onesie")

    def click_product_Tshirt_red(self):
        self.get_product_Tshirt_red().click()
        print("Click product T-shirt red")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")


    # Methods

    def select_product_backpack(self):
        self.click_product_backpack()
        self.click_cart()

    def select_product_bike_light(self):
        self.click_product_bike_light()
        self.click_cart()

