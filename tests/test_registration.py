from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators import Locators
from urls import Urls
from data import Data

class TestRegistration:
# регистрация пользователя с валидными данными
    def test_successful_registration(self, driver, wait):
        driver.get(Urls.REGISTER_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.INPUT_NAME)))
        driver.find_element(By.XPATH, Locators.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Locators.REGISTRATION_BUTN).click()
        wait.until(expected_conditions.url_to_be(Urls.LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE
# ошибка на короткий пароль при регистрации
    def test_registration_err_short_password(self, driver, wait):
        driver.get(Urls.REGISTER_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.INPUT_NAME)))
        driver.find_element(By.XPATH, Locators.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(By.XPATH, Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Locators.INPUT_PASSWORD).send_keys(Data.INVALID_PWD)
        driver.find_element(By.XPATH, Locators.REGISTRATION_BUTN).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.INVALID_PWD_ERR)))
        assert driver.find_element(By.XPATH, Locators.INVALID_PWD_ERR) is not None

