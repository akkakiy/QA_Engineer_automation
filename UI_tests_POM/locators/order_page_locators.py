from selenium.webdriver.common.by import By


class OrderPageLocators:
                    # Страница оформления заказа "Для кого самокат"
# Текст "Для кого самокат"
    TEXT_NAME = (By.XPATH, "//div[text()='Для кого самокат?']")
# Поле ввода имени
    FIELD_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
# Поле ввода фамилии
    FIELD_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
# Поле ввода адреса
    FIELD_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
# Поле ввода станции метро
    FIELD_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
# Станция метро
    STATION_METRO = (By.XPATH, ".//div[text()='Лубянка']")
    STATION_METRO_2 = (By.XPATH, ".//div[text()='Китай-город']")
# Поле ввода номера телефона
    FIELD_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
# Кнопка "Далее"
    BUTTON_NEXT = (By.XPATH, "//button[text() = 'Далее']")

                    # Страница оформления заказа "Про аренду"
# Текст "Про аренду"
    TEXT_ORDER = (By.XPATH, "//div[text()='Про аренду']")
# Поле "Когда привезти самокат"
    FIELD_WHEN = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
# Поле "Срок аренды" выподящий список
    FIELD_PERIOD = (By.XPATH, "//span[@class='Dropdown-arrow']")
# Поле "Срок аренды" двое суток
    FIELD_PERIOD_DAY = (By.XPATH, "//div[text()='трое суток']")
    FIELD_PERIOD_DAY_2 = (By.XPATH, "//div[text()='двое суток']")
# Чекбокс "Цвет самоката"
    CHECKBOX_COLOR_BLACK = (By.ID, 'black')
    CHECKBOX_COLOR_GRAY = (By.ID, 'grey')
# Поле "Комментарии для курьера"
    FIELD_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
# Кнопка "Назад"
    BUTTON_BACK = (By.XPATH, ".//button[text()='Назад']")
# Кнопка "Заказать"
    BUTTON_ORDER = (By.XPATH, "(.//button[text() = 'Заказать'])[2]")

                    # Окно подтверждения заказа
# Окно с текстом "Хотите оформить заказ?"
    ORDER_TEXT = (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
# Кнопка "Нет"
    BUTTON_NO = (By.XPATH, ".//button[text()='Нет']")
# Кнопка "Да"
    BUTTON_YES = (By.XPATH, ".//button[text()='Да']")

                    # Окно "Заказ оформлен"
# Окно оформленного заказа
    ORDER_CONFIRM = (By.XPATH, ".//div[text()='Заказ оформлен']")
# Кнопка "Посмотреть статус"
    BUTTON_STATUS = (By.XPATH, ".//button[text()='Посмотреть статус']")
# Текст "Заказ оформлен"
    ORDER_TEXT_CONFIRM = (By.XPATH, ".//div[text()='Заказ оформлен']")
