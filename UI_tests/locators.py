from selenium.webdriver.common.by import By


class Locators:
                    # ГЛАВНАЯ СТРАНИЦА

# Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, 'Конструктор')

# Логотоип/кнопка главной страницы
    MAIN_PAGE_BUTTON = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

# Кнопка "Личный кабинет"
    PROFILE_BUTTON = (By.LINK_TEXT, 'Личный Кабинет')

# Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")

# Кнопка "Булки"
    BUN_BUTTON = (By.XPATH, ".//span[text() = 'Булки']")

# Кнопка "Соусы"
    SAUCE_BUTTON = (By.XPATH, ".//span[text()='Соусы']")

# Кнопка "Начинки"
    FILLING_BUTTON = (By.XPATH, ".//span[text()='Начинки']")

# Кнопка "Оформить заказ"
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")


            # СТРАНИЦА ВХОДА В ЛИЧНЫЙ КАБИНЕТ

# Кнопка "Войти" на странице входа в личный кабинет
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти']")

# Поле ввода email при авторизации
    EMAIL_FIELD_LOGIN = (By.XPATH, ".//input[@name='name']")

# Поле ввода пароля при авторизации
    PASSWORD_FIELD_LOGIN = (By.XPATH, ".//input[@name='Пароль']")

# Кнопка "Войти" при авторизации
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

# Ссылка "Зарегистрироваться" в окне авторизации
    REGISTER_BUTTON_LOGIN = (By.XPATH, ".//a[href='/register']")

# Ссылка "Восстановить пароль" в окне авторизации
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, ".//a[href='/forgot-password']")

# Поле ввода email при восстановлении пароля
    EMAIL_FIELD_RECOVERY = (By.XPATH, ".//input[@name='name']")

# Кнопка "Восстановить" при восстановлении пароля
    RECOVERY_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

# Ссылка "Войти" если вспомнил пароль
    LOGIN_BUTTON_RECOVERY = (By.XPATH, ".//a[text() = 'Войти']")


            # СТРАНИЦА РЕГИСТРАЦИИ

# Поле ввода логина при регистрации
    LOGIN_FIELD = (By.XPATH, ".//input[../label='Имя']")

# Поле ввода email при регистрации
    EMAIL_FIELD = (By.XPATH, ".//input[../label='Email']")

# Поле ввода пароля при регистрации
    PASSWORD_FIELD = (By.XPATH, ".//input[../label='Пароль']")

# Кнопка "Зарегистрироваться" при регистрации
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

# Ссылка "Войти" на странице регистрации
    LOGIN_BUTTON_REGISTRATION = (By.XPATH, ".//a[text() = 'Войти']")


            # СООБЩЕНИЯ ОБ ОШИБКАХ

# Некорректный пароль
    INCORRECT_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")

# Повторная регистрация пользователя
    REPEATED_REGISTRATION = (By.XPATH, ".//p[text()='Такой пользователь уже существует']")



            # СТРАНИЦА ЛИЧНОГО КАБИНЕТА
# Ссылка на профиль в личном кабинете
    PROFILE_LINK = (By.XPATH, ".//a[href='/account/profile']")

# Ссылка на историю заказов в личном кабинете
    ORDERS_HISTORY_LINK = (By.XPATH, ".//a[href='/account/order-history']")

# Кнопка "Сохранить" в личном кабинете
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")

# Кнопка "Выход" в личном кабинете
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")

# Окно ввода имеени "Имя"
    NAME_FIELD = (By.XPATH, "../label[text()='Имя']")
