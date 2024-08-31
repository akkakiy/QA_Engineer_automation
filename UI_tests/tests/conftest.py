import pytest


@pytest.fixture(scope="function")
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()