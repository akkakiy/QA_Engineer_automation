from UI_tests.locators import Locators
from UI_tests.urls import URL


class TestConstructor:
    def test_constructor_buns(self, driver):     #Проверка кнопки "Булки"
        driver.get(URL.main_page)
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        driver.find_element(*Locators.BUN_BUTTON).click()
        text_bun = driver.find_element(*Locators.BUN_BUTTON).text
        displayed_bun = driver.find_element(*Locators.BUN_BUTTON).is_displayed()
        assert text_bun == 'Булки' and displayed_bun

    def test_constructor_sauces(self, driver):       #Проверка кнопки "Соусы"
        driver.get(URL.main_page)
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        text_sauce = driver.find_element(*Locators.SAUCE_BUTTON).text
        displayed_sauce = driver.find_element(*Locators.SAUCE_BUTTON).is_displayed()
        assert text_sauce == 'Соусы' and displayed_sauce

    def test_constructor_fillings(self, driver):     #Проверка кнопки "Начинки"
        driver.get(URL.main_page)
        driver.find_element(*Locators.FILLING_BUTTON).click()
        text_filling = driver.find_element(*Locators.FILLING_BUTTON).text
        displayed_filling = driver.find_element(*Locators.FILLING_BUTTON).is_displayed()
        assert text_filling == 'Начинки' and displayed_filling
