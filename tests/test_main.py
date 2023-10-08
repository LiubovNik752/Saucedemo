import time
import pytest
from pages.login_page import link
from pages.main_page import Main_page


class Test_main_page:

    # @pytest.mark.parametrize("get_product_name, click_product", [
    #                                                             (get_product_name_backpack(), click_product_backpack()),
    #                                                             (get_product_name_bike_light(), click_product_bike_light()),
    #                                                             (get_product_name_tshirt_black(), click_product_tshirt_black()),
    #                                                             (get_product_name_fleece_jacket(), click_product_fleece_jacket()),
    #                                                             (get_product_name_onesie(), click_product_onesie()),
    #                                                             (get_product_name_tshirt_red(), click_product_tshirt_red())
    #                                                             ]
    #                          )
    # def test_add_product(self, check_in, get_product_name, click_product):
    #     page = Main_page(check_in, link)
    #     main_page_name = page.get_product_name
    #     page.click_product
    #     page.click_cart_icon()
    #     time.sleep(2)
    #     page.get_screenshot()
    #     cart_page_name = page.get_cart_product_name()
    #     assert main_page_name == cart_page_name

    @pytest.mark.smoke
    def test_add_product(self, check_in):
        page = Main_page(check_in, link)
        main_page_name = page.get_product_name_backpack()
        page.click_product_backpack()
        page.click_cart_icon()
        time.sleep(2)
        page.get_screenshot()
        cart_page_name = page.get_cart_product_name()
        assert main_page_name == cart_page_name

    @pytest.mark.smoke
    def test_counter(self, check_in):
        counter = 0
        page = Main_page(check_in, link)
        page.click_product_backpack()
        counter += 1
        page.click_product_bike_light()
        counter += 1
        assert page.get_cart_counter() == str(counter)

    @pytest.mark.extra
    def test_sort_price_growth(self, check_in):
        page = Main_page(check_in, link)
        page.click_sort_btn()
        page.click_sort_price_lohi()
        value = page.get_list_price()
        assert value == sorted(value)   # Проверка что список цен равен отсортированному по возрастанию списку цен

    @pytest.mark.extra
    def test_sort_price_decrease(self, check_in):
        page = Main_page(check_in, link)
        page.click_sort_btn()
        page.click_sort_price_hilo()
        value = page.get_list_price()
        assert value == sorted(value, reverse=True)   # Проверка что список цен равен отсортированному по убыванию списку цен

    @pytest.mark.extra
    def test_sort_products_az(self, check_in):
        page = Main_page(check_in, link)
        page.click_sort_btn()
        page.click_sort_name_az()
        value = page.get_list_names()
        assert value == sorted(value)  # Проверка что список названий товаров равен отсортированному по возрастанию списку товаров

    @pytest.mark.extra
    def test_sort_products_za(self, check_in):
        page = Main_page(check_in, link)
        page.click_sort_btn()
        page.click_sort_name_az()
        value = page.get_list_names()
        assert value == sorted(value, reverse=True) # Проверка что список названий товаров равен отсортированному по убыванию списку товаров