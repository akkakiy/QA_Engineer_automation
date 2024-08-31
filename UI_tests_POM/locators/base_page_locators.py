from selenium.webdriver.common.by import By


class BasePageLocators:
#Локатор кнопки принятия куки "да все привыкли"
    ACCEPT_COOKIES_BUTTON = (By.ID, 'rcc-confirm-button')
#Локатор кнопки "Заказать" в шапке страницы
    ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
#Кнопка "Статус заказа"
    STATUS_ORDER_BUTTON = (By.CLASS_NAME, 'Header_Link__1TAG7')
#Лого Яндекс Дзен
    DZEN_TEXT = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
#Ссылка на главную страницу Яндекс Дзен
    DZEN_LINK = (By.XPATH, ".//a[@href='//yandex.ru']")
#Ссылка на главную страницу Яндекс Самокат
    SCOOTER_LINK = (By.XPATH, ".//a[@href='/']")
#Поле ввода номера заказа
    ORDER_NUMBER = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
#Кнопка "GO!"
    GO_BUTTON = (By.LINK_TEXT, 'GO!')
#Кнопка "Зказать" в теле страницы
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(.//button[text() = 'Заказать'])[2]")
