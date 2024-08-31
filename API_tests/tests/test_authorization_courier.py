import allure
import pytest
import requests

from API_tests.data import Endpoints, Massages
from API_tests.help import FullLifeCourier, CreateRandomCourier


class TestsLoginCourier:
    @allure.title("Тест авторизации созданного курьера с заполнением всех обязательных полей")
    def test_login_valid_courier(self, courier_cycle):
        assert courier_cycle[1].status_code == 200 and courier_cycle[1].json()["id"]

    @allure.title("Тест ошибки при авторизации курьера без заполнения одного из обязательных полей")
    @pytest.mark.parametrize("courier_without_field", [FullLifeCourier.invalid_courier_without_login,
                                                       FullLifeCourier.invalid_courier_without_password])
    def test_login_without_field(self, courier_without_field):
        response = requests.post(f"{Endpoints.LOGIN_URL}", data=courier_without_field)
        assert response.status_code == 400 and Massages.LOGIN_ERROR_MESSAGE in response.text

    @allure.title("Тест авторизации несуществующего курьера")
    def test_login_nonexistent_courier(self):
        courier = CreateRandomCourier.create_nonexistent_courier()
        response = requests.post(f"{Endpoints.LOGIN_URL}", data=courier)
        assert response.status_code == 404 and Massages.LOGIN_ERROR_MESSAGE_NOT_FOUND in response.text
