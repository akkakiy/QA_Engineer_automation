from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from UI_tests.constants import MainUser
from UI_tests.locators import Locators
from UI_tests.urls import URL


class TestProfile:
    def test_click_profile(self, driver):       #Проверка перехода в личный кабинет через кнопку "Личный кабинет"
        driver.get(URL.main_page)
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(MainUser.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(MainUser.PASS_USER)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON)).is_displayed()
        assert driver.find_element(*Locators.EXIT_BUTTON).is_displayed()

    def test_click_constructor(self, driver):       # Переход из личного кабинета в конструктор
        driver.get(URL.main_page)
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(MainUser.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(MainUser.PASS_USER)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON)).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_BUTTON)).is_displayed()
        assert driver.find_element(*Locators.MAIN_PAGE_BUTTON).is_displayed()

    def test_click_main_page(self, driver):       # Переход из личного кабинета на главную страницу при клике на логотип
        driver.get(URL.main_page)
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(MainUser.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(MainUser.PASS_USER)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON)).click()
        driver.find_element(*Locators.MAIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_PAGE_BUTTON)).is_displayed()
        assert driver.find_element(*Locators.MAIN_PAGE_BUTTON).is_displayed()

    def test_click_exit(self, driver):            # Выход из аккаунта
        driver.get(URL.main_page)
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD_LOGIN).send_keys(MainUser.EMAIL_USER)
        driver.find_element(*Locators.PASSWORD_FIELD_LOGIN).send_keys(MainUser.PASS_USER)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_ACCOUNT_BUTTON))
        assert driver.current_url == URL.login_page
