from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators import Locators
from urls import Urls
from data import Data

# выход по кнопке «Выйти» в личном кабинете
class TestLogout:
    def test_logout_button_exit_lk(self,driver, wait):
        driver.get(Urls.LOGIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.INPUT_AUTH_LOGIN)))
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_LOGIN).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_PASS).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Locators.ENTER_BUTN).click()
        driver.find_element(By.XPATH, Locators.LK_BUTN).click()
        wait.until(expected_conditions.url_to_be(Urls.PROFILE_PAGE))
        driver.find_element(By.XPATH, Locators.EXIT_LK_BUTN).click()
        wait.until(expected_conditions.url_to_be(Urls.LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE
