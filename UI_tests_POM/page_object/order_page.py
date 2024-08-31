import allure

from UI_tests_POM.locators.order_page_locators import OrderPageLocators
from UI_tests_POM.page_object.base_page import BasePage


class PageOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение поля "Имя"')
    def fill_name(self, name):
        self.fill_elements(OrderPageLocators.FIELD_NAME, name)

    @allure.step('Заполнение поля "Фамилия"')
    def fill_surname(self, surname):
        self.fill_elements(OrderPageLocators.FIELD_SURNAME, surname)

    @allure.step('Заполнение поля "Адрес"')
    def fill_address(self, address):
        self.fill_elements(OrderPageLocators.FIELD_ADDRESS, address)

    @allure.step('Выбор станции метро')
    def select_metro_station(self):
        self.find_element(OrderPageLocators.FIELD_METRO).click()
        self.find_element(OrderPageLocators.STATION_METRO).click()

    @allure.step('Заполнение поля "Телефон"')
    def fill_phone(self, phone):
        self.fill_elements(OrderPageLocators.FIELD_PHONE, phone)

    @allure.step('Нажатие на кнопку "Далее"')
    def click_next_button(self):
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение поля "Когда привезти самокат"')
    def fill_when(self, when):
        self.fill_elements(OrderPageLocators.FIELD_WHEN, when)

    @allure.step('Заполнение поля "Срок аренды"')
    def fill_period(self):
        self.find_element(OrderPageLocators.FIELD_PERIOD).click()
        self.find_element(OrderPageLocators.FIELD_PERIOD_DAY).click()

    @allure.step('Выбор цвета')
    def select_color(self):
        self.find_element(OrderPageLocators.CHECKBOX_COLOR_GRAY).click()

    @allure.step('Заполнение поля "Комментарий для курьера"')
    def fill_comment(self, comment):
        self.fill_elements(OrderPageLocators.FIELD_COMMENT, comment)

    @allure.step('Нажатие на кнопку "Заказать"')
    def click_order_button(self):
        self.click_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Нажатие на кнопку "Да"')
    def click_yes_button(self):
        self.click_element(OrderPageLocators.BUTTON_YES)

    @allure.step('Полное оформление заказа')
    def full_fill_order(self, user):
        self.fill_name(user['name'])
        self.fill_surname(user['surname'])
        self.fill_address(user['address'])
        self.select_metro_station()
        self.fill_phone(user['phone'])
        self.click_next_button()
        self.fill_when(user['when'])
        self.fill_period()
        self.select_color()
        self.fill_comment(user['comment'])
        self.click_order_button()
        self.click_yes_button()

    @allure.step('Проверка оформленного заказа')
    def check_order(self):
        return self.get_text(OrderPageLocators.ORDER_CONFIRM)
