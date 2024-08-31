class Endpoints:
    URL = 'https://qa-scooter.praktikum-services.ru/'

    LOGIN_URL = f"{URL}api/v1/courier/login"

    CREATING_URL = f"{URL}api/v1/courier"

    CREATING_ORDER_URL = f"{URL}api/v1/orders"

    DELETE_URL = f"{URL}api/v1/courier/"

    ORDER_LIST_URL = f"{URL}api/v1/orders"

    ACCEPT_ORDER_URL = f"{URL}api/v1/orders/accept/"

    GET_ORDER_URL = f"{URL}api/v1/orders/track"


class Massages:
    CREATE_ERROR_MESSAGE_DUPLICATE = "Этот логин уже используется. Попробуйте другой."
    CREATE_ERROR_MESSAGE = "Недостаточно данных для создания учетной записи"
    LOGIN_ERROR_MESSAGE_NOT_FOUND = "Учетная запись не найдена"
    LOGIN_ERROR_MESSAGE = "Недостаточно данных для входа"
    DELETE_ERROR_MESSAGE = "Курьера с таким id нет"
    ACCEPT_ORDER_ERROR_MESSAGE_NO_ID = "Недостаточно данных для поиска"
    ACCEPT_ORDER_ERROR_MESSAGE_NO_COURIER = "Курьера с таким id не существует"
    ACCEPT_ORDER_ERROR_MESSAGE_INCORRECT_ORDER_ID = "Заказа с таким id не существует"
    GET_ORDER_ERROR_MESSAGE_NO_ID = "Недостаточно данных для поиска"
    GET_ORDER_ERROR_MESSAGE_INCORRECT_ORDER_ID = "Заказ не найден"



