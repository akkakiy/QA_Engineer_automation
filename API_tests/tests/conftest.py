import json

import allure
import pytest
import requests

from API_tests.data import Endpoints
from API_tests.help import FullLifeCourier


@allure.title('Создание, авторизация и удаление курьера')
@pytest.fixture(scope='function')
def courier_cycle():
    create_courier = requests.post(f"{Endpoints.CREATING_URL}", data=FullLifeCourier.valid_courier)
    login_courier = requests.post(f"{Endpoints.LOGIN_URL}", data=FullLifeCourier.valid_courier)
    id_courier = login_courier.json()["id"]
    yield create_courier, login_courier
    delete_courier = requests.delete(f"{Endpoints.DELETE_URL}{id_courier}")


@allure.title('Создание и авторизация курьера')
@pytest.fixture(scope='function')
def courier_create():
    create_courier = requests.post(f"{Endpoints.CREATING_URL}", data=FullLifeCourier.valid_courier)
    login_courier = requests.post(f"{Endpoints.LOGIN_URL}", data=FullLifeCourier.valid_courier)
    id_courier = login_courier.json()["id"]
    yield id_courier


@allure.title('Создание заказа')
@pytest.fixture(scope='function')
def create_order():
    headers = {'Content-type': 'application/json'}
    data_client = {
        'name': 'Октавиан',
        'surname': 'Август',
        'address': 'город Рим, улица Фиренце, дом 116',
        'metro_station': 1,
        'phone': '+7 999 888 77 66',
        'period': 3,
        'when': "2024-09-01",
        'comment': "Аве мне!",
        'color': ['GRAY'],
    }
    data_client = json.dumps(data_client)
    response = requests.post(f"{Endpoints.CREATING_ORDER_URL}", data=data_client, headers=headers)
    order_id = response.json()["track"]
    yield order_id
