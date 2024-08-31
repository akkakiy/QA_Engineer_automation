import allure
import requests

from API_tests.data import Endpoints, Massages


class TestAcceptOrder:
    @allure.title("Тест принятие заказа")                                   #иногда падает с ошибками 404 и 409
    def test_accept_order(self, courier_create, create_order):
        accept_order = requests.put(f"{Endpoints.ACCEPT_ORDER_URL}{create_order}?courierId={courier_create}")
        assert accept_order.status_code == 200 and accept_order.text == '{"ok":true}'

    @allure.title("Тест принятие заказа без ID курьера")
    def test_accept_order_no_id_courier(self, create_order):
        courier_no_id = ''
        accept_order = requests.put(f"{Endpoints.ACCEPT_ORDER_URL}{create_order}?courierId={courier_no_id}")
        assert accept_order.status_code == 400 and Massages.ACCEPT_ORDER_ERROR_MESSAGE_NO_ID

    @allure.title("Тест принятие заказа с некорректным ID курьера")
    def test_accept_order_incorrect_id_courier(self, create_order):
        courier_incorrect_id = '965'
        accept_order = requests.put(f"{Endpoints.ACCEPT_ORDER_URL}{create_order}?courierId={courier_incorrect_id}")
        assert accept_order.status_code == 404 and Massages.ACCEPT_ORDER_ERROR_MESSAGE_NO_COURIER

    @allure.title("Тест принятие заказа с несуществующим ID")
    def test_accept_order_incorrect_order_id(self, courier_create):
        order_id = '4561000'
        accept_order = requests.put(f"{Endpoints.ACCEPT_ORDER_URL}{order_id}?courierId={courier_create}")
        assert accept_order.status_code == 404 and Massages.ACCEPT_ORDER_ERROR_MESSAGE_INCORRECT_ORDER_ID

    @allure.title("Тест принятие заказа без ID")
    def test_accept_order_no_id_order(self, courier_create):
        accept_order = requests.put(f"{Endpoints.ACCEPT_ORDER_URL}courierId={courier_create}")
        assert accept_order.status_code == 400 and Massages.ACCEPT_ORDER_ERROR_MESSAGE_NO_ID


class TestGetOrder:
    @allure.title("Тест получение заказа по номеру")
    def test_get_order(self, create_order):
        get_order = requests.get(f"{Endpoints.GET_ORDER_URL}?t={create_order}")
        assert get_order.status_code == 200 and 'order' in get_order.text

    @allure.title("Тест получение заказа без номера")
    def test_get_order_no_id(self):
        get_order = requests.get(f"{Endpoints.GET_ORDER_URL}?t=")
        assert get_order.status_code == 400 and Massages.GET_ORDER_ERROR_MESSAGE_NO_ID

    @allure.title("Тест получение заказа с несуществующим номером")
    def test_get_order_incorrect_id(self):
        order_id = '4561000'
        get_order = requests.get(f"{Endpoints.GET_ORDER_URL}?t={order_id}")
        assert get_order.status_code == 404 and Massages.GET_ORDER_ERROR_MESSAGE_INCORRECT_ORDER_ID
