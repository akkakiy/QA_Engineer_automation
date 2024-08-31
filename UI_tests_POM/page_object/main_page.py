import allure

from UI_tests_POM.help.data import Urls
from UI_tests_POM.locators.base_page_locators import BasePageLocators
from UI_tests_POM.locators.questions_page_locators import LocatorsQuestions
from UI_tests_POM.page_object.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка URL главной страницы')
    def checking_url_main(self):
        return self.go_to_url(Urls.BASE_URL)

    @allure.step('Проверка URL оформления заказа')
    def checking_url_order(self):
        return self.check_to_url(Urls.ORDER_URL)

    @allure.step('Поиск кнопки "Заказать" в шапке страницы')
    def find_order_button(self):
        return self.find_element(BasePageLocators.ORDER_BUTTON)

    @allure.step('Клик по кнопке "Заказать" в шапке сайта')
    def click_order_button(self):
        self.click_element(BasePageLocators.ORDER_BUTTON)

    @allure.step('Полное открытие страницы оформления заказа через кнопку "Заказать" в шапке страницы')
    def full_open_order_page_header(self):
        self.checking_url_main()
        self.find_order_button()
        self.click_order_button()

    @allure.step('Скролл на кнопку "Заказать" в теле страницы')
    def scroll_to_order_button(self):
        self.scroll_to_element(BasePageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Клик по кнопке "Заказать" в теле страницы')
    def click_to_order_button(self):
        self.click_element(BasePageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Полное открытие страницы оформления заказа через кнопку "Заказать" в теле страницы')
    def full_open_order_page_footer(self):
        self.checking_url_main()
        self.scroll_to_order_button()
        self.click_to_order_button()

    @allure.step('Принятия куки')
    def accept_cookies(self):
        self.find_element(BasePageLocators.ACCEPT_COOKIES_BUTTON)
        self.click_element(BasePageLocators.ACCEPT_COOKIES_BUTTON)


class QuestionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Скролл в раздел "Вопросы о важном" в теле страницы')
    def scroll_to_order_questions(self):
        self.scroll_to_element(LocatorsQuestions.QUESTIONS)

    @allure.step('Получение текста "Вопросы о важном"')
    def get_text_questions(self):
        return self.get_text(LocatorsQuestions.QUESTIONS)

    @allure.step('Клик на вопрос')
    def click_to_order_button(self, number_question):
        self.scroll_to_order_questions()
        self.click_element(LocatorsQuestions.BUTTONS_QUESTION[number_question])
        self.click_element(LocatorsQuestions.ANSWERS[number_question])

    @allure.step('Получение ответа')
    def get_answer(self, number_question):
        self.scroll_to_order_questions()
        return self.get_text(LocatorsQuestions.ANSWERS[number_question])
