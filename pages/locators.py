from selenium.webdriver.common.by import By


class Login_page_locators:
    user_name = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    login_button = (By.XPATH, "//input[@id='login-button']")
    main_word = (By.XPATH, "//div[@class='app_logo']")
    locked_word = (By.XPATH, "//h3[@data-tests='error']")
    error_text = (By.XPATH, "//h3[@data-test='error']")


class Main_page_locators:
    burger_menu_button = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    logout_button = (By.CSS_SELECTOR, "#logout_sidebar_link")

    backpack_btn = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    bike_light_btn = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
    tshirt_black_btn = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    fleece_jacket_btn = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket")
    onesie_btn = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    tshirt_red_btn = (By.XPATH, "//*[contains(@id, 't-shirt-(red)')]")

    product_name_backpack = (By.XPATH, "//*[contains(text(), 'Backpack')]")
    product_name_bike_light = (By.XPATH, "//*[contains(text(), 'Bike Light')]")
    product_name_tshirt_black = (By.XPATH, "//*[contains(text(), 'Bolt T-Shirt')]")
    product_name_fleece_jacket = (By.XPATH, "//*[contains(text(), 'Fleece Jacket')]")
    product_name_onesie = (By.XPATH, "//*[contains(text(), 'Onesie')]")
    product_name_tshirt_red = (By.XPATH, "//*[contains(text(), 'T-Shirt (Red)')]")

    cart_icon = (By.XPATH, "//a[@class='shopping_cart_link']")
    cart_counter = (By.XPATH, "//span[@class='shopping_cart_badge']")

    sort_btn = (By.XPATH, "//select[@class='product_sort_container']")
    select = (By.TAG_NAME, "select")
    product_price = (By.XPATH, "//div[@class='inventory_item_price']")
    product_name = (By.XPATH, "//div[@class='inventory_item_name']")


class Cart_page_locators:
    product_name = (By.XPATH, "//div[@class='inventory_item_name']")
