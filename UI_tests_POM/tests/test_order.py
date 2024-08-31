import allure

from UI_tests_POM.help.data import ORDER_CONFIRM, User
from UI_tests_POM.page_object.main_page import MainPage
from UI_tests_POM.page_object.order_page import PageOrder


class TestOrderPageHeader:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в шапке сайта')
    def test_order_page_name_name(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.full_open_order_page_header()
        page_order = PageOrder(driver)
        page_order.full_fill_order(User.user_1)
        assert ORDER_CONFIRM in page_order.check_order()


class TestOrderPageFooter:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в теле сайта')
    def test_order_page_name_name(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.full_open_order_page_footer()
        page_order = PageOrder(driver)
        page_order.full_fill_order(User.user_2)
        assert ORDER_CONFIRM in page_order.check_order()
