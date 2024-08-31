from selenium.webdriver.common.by import By


class LocatorsDzen:
#Кнопка "Москва"
    MOSCOW_DZEN = (By.LINK_TEXT, 'Москва')
#Панель с выбором новостей
    NEWS_DZEN = (By.XPATH, "//div[@class='side-shadow-wrapper__childContainer-1Y']")
