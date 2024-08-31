import allure
import pytest
import requests

from API_tests.data import Endpoints, Massages
from API_tests.help import FullLifeCourier, Courier


class TestsCreateCourier:
    @allure.title("Тест возможности создания курьера с заполнением всех полей")
    def test_create_valid_courier(self, courier_cycle):
        assert courier_cycle[0].status_code == 201 and courier_cycle[0].text == '{"ok":true}'

    @allure.title("Тест возможности создания курьера без заполнения поля имени")
    def test_create_courier_without_name(self):
        courier = FullLifeCourier.invalid_courier_without_first_name
        response = requests.post(f"{Endpoints.CREATING_URL}", data=courier)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title("Тест ошибки при создания курьера с существующим логином")
    def test_create_duplicate_courier(self, courier_cycle):
        create_courier = Courier.create_courier()
        assert create_courier["status_code"] == 409 and Massages.CREATE_ERROR_MESSAGE_DUPLICATE

    @allure.title("Тест ошибки при создании курьера без заполнения одного из обязательных полей")
    @pytest.mark.parametrize("courier_without_field", [FullLifeCourier.invalid_courier_without_login,
                                                       FullLifeCourier.invalid_courier_without_password])
    def test_create_courier_without_field(self, courier_without_field):
        response = requests.post(f"{Endpoints.CREATING_URL}", data=courier_without_field)
        assert response.status_code == 400 and Massages.CREATE_ERROR_MESSAGE in response.text
