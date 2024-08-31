import allure

from UI_tests_POM.locators.base_page_locators import BasePageLocators
from UI_tests_POM.locators.dzen_page_locators import LocatorsDzen
from UI_tests_POM.page_object.base_page import BasePage


class SwitchWindowPage(BasePage):
    @allure.step('Переход на главную страницу Дзен')
    def find_and_click_on_the_dzen_button(self):
        self.find_element(BasePageLocators.DZEN_TEXT)
        self.click_element(BasePageLocators.DZEN_LINK)
        self.go_to_page(-1)

    @allure.step('Переход на главную страницу Самокат')
    def go_to_main_page_scooter(self):
        self.click_element(BasePageLocators.SCOOTER_LINK)

    @allure.step('Проверка заголовков новостей')
    def check_to_news(self):
        return self.find_element(LocatorsDzen.MOSCOW_DZEN).text
