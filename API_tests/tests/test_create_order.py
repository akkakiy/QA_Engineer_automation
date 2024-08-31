import json
import allure
import pytest
import requests

from API_tests.data import Endpoints
from API_tests.help import CreateClient


class TestCreateOrder:
    @allure.title("Тест создания заказа с разными цветами")
    @pytest.mark.parametrize('color', [['BLACK'], ['GRAY'], ['BLACK', 'GRAY'], ['']])
    def test_create_order(self, color):
        headers = {'Content-type': 'application/json'}
        data_client = CreateClient.client
        data_client['color'] = color
        data_client = json.dumps(data_client)
        response = requests.post(f"{Endpoints.CREATING_ORDER_URL}", data=data_client, headers=headers)
        assert response.status_code == 201 and 'track' in response.text


class TestListOrder:
    @allure.title("Тест получение списка заказов")
    def test_get_order_list(self):
        response = requests.get(f"{Endpoints.ORDER_LIST_URL}")
        assert response.status_code == 200 and 'track' in response.text
