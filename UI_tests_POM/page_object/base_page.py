import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу')
    def go_to_url(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Проверка URL')
    def check_to_url(self):
        return self.driver.current_url

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step('Заполнить значение')
    def fill_elements(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Ввод информации в поле')
    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Получение текста')
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Скролл на элемент')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переход на другую вкладку')
    def go_to_page(self, new_page):
        self.driver.switch_to.window(self.driver.window_handles[new_page])
