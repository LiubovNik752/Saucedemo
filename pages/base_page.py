import datetime


class Base_page:
    def __init__(self, driver, link):
        self.link = link
        self.driver = driver

    # Открытие страницы

    def open_url(self):
        self.driver.get(self.link)

    # Клик на элемент

    def click_element(self, method, locator):
        self.driver.find_element(method, locator).click()

    # Передача текста в поле ввода

    def input_text(self, method, locator, text):
        self.driver.find_element(method, locator).send_keys(text)

    # Скриншот страницы

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("_%H-%M-%S.%d.%m.%y.")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Lubov\\PycharmProjects\\PythonProject1\\screens' + name_screenshot)

    # Проверка текущего адреса страницы

    def assert_current_page(self, link):
        assert link in self.driver.current_url