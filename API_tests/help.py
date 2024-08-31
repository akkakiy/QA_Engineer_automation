import requests

from faker import Faker
from data import Endpoints


class CreateRandomCourier:
    @staticmethod
    def create_random_valid_courier():      # создаем курьера с рандомными валидными данными
        fake = Faker('ru_RU')
        courier = {
            "login": fake.user_name(),
            "password": fake.password(),
            "first_name": fake.first_name(),
        }
        return courier

    @staticmethod
    def create_random_invalid_courier_without_login():      # создаем курьера без логина
        fake = Faker('ru_RU')
        courier = {
            "login": "",
            "password": fake.password(),
            "first_name": fake.first_name(),
        }
        return courier

    @staticmethod
    def create_random_invalid_courier_without_password():       # создаем курьера без пароля
        fake = Faker('ru_RU')
        courier = {
            "login": fake.user_name(),
            "password": "",
            "first_name": fake.first_name(),
        }
        return courier

    @staticmethod
    def create_random_invalid_courier_without_first_name():       # создаем курьера без имени
        fake = Faker('ru_RU')
        courier = {
            "login": fake.user_name(),
            "password": fake.password(),
            "first_name": "",
        }
        return courier

    @staticmethod
    def create_nonexistent_courier():       # создаем несуществующего курьера
        nonexistent_courier = {
            "login": "nonexistent",
            "password": "nonexistent",
            "first_name": "nonexistent"
        }
        return nonexistent_courier


class FullLifeCourier:        # данные для создания курьера
    valid_courier = CreateRandomCourier.create_random_valid_courier()
    invalid_courier_without_login = CreateRandomCourier.create_random_invalid_courier_without_login()
    invalid_courier_without_password = CreateRandomCourier.create_random_invalid_courier_without_password()
    invalid_courier_without_first_name = CreateRandomCourier.create_random_invalid_courier_without_first_name()
    nonexistent_courier = CreateRandomCourier.create_nonexistent_courier()


class Courier:
    @staticmethod
    def create_courier():       # регистрация курьера
        courier = FullLifeCourier.valid_courier
        response = requests.post(f"{Endpoints.CREATING_URL}", data=courier)
        return {"response_text": response.text, "status_code": response.status_code, "data_courier": courier}

    @staticmethod
    def login_courier(courier):        # авторизация курьера
        response = requests.post(f"{Endpoints.LOGIN_URL}", data=courier)
        return {"id": str(response.json()["id"]), "response_text": response.text, "status_code": response.status_code}

    @staticmethod
    def delete_courier(courier_id):        # удаление курьера
        response = requests.delete(f"{Endpoints.DELETE_URL}{courier_id}")
        return {"response_text": response.text, "status_code": response.status_code}


class CreateClient:       # данные для создания клиента
    client = {
        'name': 'Октавиан',
        'surname': 'Август',
        'address': 'город Рим, улица Фиренце, дом 116',
        'metro_station': 1,
        'phone': '+7 999 888 77 66',
        'period': 3,
        'when': "2024-09-01",
        'comment': "Аве мне!",
        'color': ["GREY"],
    }
