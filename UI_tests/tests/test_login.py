from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from UI_tests.constants import MainUser
from UI_tests.locators import Locators
from UI_tests.urls import URL


class TestLogin:
    def test_login_personal_account(self, driver):       #Проверка авторизации через кнопку "Личный кабинет"
        driver.get(URL.main_page)
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(MainUser.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(MainUser.PASS_USER)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert driver.current_url == URL.main_page and order_button == 'Оформить заказ'

    def test_login_main_page(self, driver):     #Проверка авторизации через кнопку "Войти в аккаунт"
        driver.get(URL.main_page)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(MainUser.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(MainUser.PASS_USER)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert driver.current_url == URL.main_page and order_button == 'Оформить заказ'

    def test_login_registration_page(self, driver):     #Проверка авторизации со страницы регистрации
        driver.get(URL.registration_page)
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION).click()
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(MainUser.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(MainUser.PASS_USER)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert driver.current_url == URL.main_page and order_button == 'Оформить заказ'

    def test_login_pass_page(self, driver):     #Провера авторизации со страницы восстановления пароля
        driver.get(URL.password_recovery_page)
        driver.find_element(*Locators.LOGIN_BUTTON_RECOVERY).click()
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(MainUser.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(MainUser.PASS_USER)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).text
        assert driver.current_url == URL.main_page and order_button == 'Оформить заказ'
