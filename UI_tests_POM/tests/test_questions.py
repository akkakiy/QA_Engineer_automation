import pytest
import allure

from UI_tests_POM.help.data import Questions
from UI_tests_POM.page_object.main_page import MainPage, QuestionsPage


class TestMainPage:
    @allure.title('Проверка соответствия текста ответа вопросу')
    @allure.description('На странице ищем вопрос по номеру, кликаем на него и получаем текст ответа, проверяем его соответствие вопросу')
    @pytest.mark.parametrize('num, answer_text', Questions.list_answers)
    def test_answers_to_questions(self, driver, num, answer_text):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        questions_page = QuestionsPage(driver)
        questions_page.scroll_to_order_questions()
        questions_page.click_to_order_button(num)
        assert questions_page.get_answer(num) == answer_text
