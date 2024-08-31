from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UI_tests.constants import RandomUser, MainUser
from UI_tests.locators import Locators
from UI_tests.urls import URL


class TestRegistration:     #Проверка регистрации случайного пользователя
    def test_registration(self, driver):
        driver.get(URL.registration_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(RandomUser.NAME_RANDOM_USER)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(RandomUser.EMAIL_RANDOM_USER)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(RandomUser.PASS_RANDOM_USER)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        login_page = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON)).is_displayed()
        assert driver.current_url == URL.login_page and login_page

    def test_registration_main_user(self, driver):      #Проверка регистрации существующего пользователя
        driver.get(URL.registration_page)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(MainUser.NAME_USER)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(MainUser.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(MainUser.PASS_USER)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REPEATED_REGISTRATION))
        error = driver.find_element(*Locators.REPEATED_REGISTRATION).text
        assert error == 'Такой пользователь уже существует'

    def test_login_with_incorrect_registration_error(self, driver):     #Регистрация пользователя с некорректным паролем
        driver.get(URL.registration_page)
        driver.find_element(*Locators.LOGIN_FIELD).send_keys(RandomUser.NAME_RANDOM_USER)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(RandomUser.EMAIL_RANDOM_USER)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('12345')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD))
        error = driver.find_element(*Locators.INCORRECT_PASSWORD).text
        assert error == 'Некорректный пароль'
