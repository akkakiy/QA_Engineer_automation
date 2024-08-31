import allure
import requests

from API_tests.data import Massages, Endpoints
from API_tests.help import Courier


class TestDeleteCourier:
    @allure.title("Тест создания и удаления курьера")
    def test_delete_courier_success(self):
        courier = Courier.create_courier()
        login_courier = Courier.login_courier(courier["data_courier"])
        id_courier = login_courier["id"]
        response = Courier.delete_courier(id_courier)
        assert response["status_code"] == 200 and response["response_text"] == '{"ok":true}'

    @allure.title("Тест удаления несуществующего курьера")
    def test_delete_invalid_courier(self):
        courier_id = '123456'
        response = Courier.delete_courier(courier_id)
        assert response["status_code"] == 404 and Massages.DELETE_ERROR_MESSAGE in response["response_text"]

    @allure.title("Тест удаления курьера с пустым id")
    def test_delete_courier_none_id_failed(self):
        response = requests.delete(f"{Endpoints.DELETE_URL}/")
        assert response.status_code == 404 and response.text == '{"code":404,"message":"Not Found."}'
                #не соответствует документации, код ошибки 400, текст ошибки "Недостаточно данных для удаления курьера"
