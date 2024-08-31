import allure

from UI_tests_POM.help.data import MOSCOW_DZEN, QUESTIONS
from UI_tests_POM.page_object.main_page import MainPage, QuestionsPage
from UI_tests_POM.page_object.switch_page import SwitchWindowPage


class TestLinkDzen:
    @allure.title('Проверка переключения на страницу "Дзен"')
    def test_dzen_link(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        switch_window = SwitchWindowPage(driver)
        switch_window.find_and_click_on_the_dzen_button()
        text_url = switch_window.check_to_news()
        assert text_url == MOSCOW_DZEN


class TestLinkScooter:
    @allure.title('Проверка переключения на страницу "Самокат"')
    def test_scooter_link(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.full_open_order_page_header()
        page = SwitchWindowPage(driver)
        page.go_to_main_page_scooter()
        questions_page = QuestionsPage(driver)
        questions_page.scroll_to_order_questions()
        text_questions = questions_page.get_text_questions()
        assert text_questions == QUESTIONS
