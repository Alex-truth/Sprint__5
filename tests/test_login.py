from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators import Locators
from urls import Urls
from data import Data

# логин с главной страницы
class TestLogIn:
    def test_login_button_main_page(self, driver, wait):
        driver.get(Urls.OWN_SITE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOG_IN_MAIN_PAGE_BUTN)))
        driver.find_element(By.XPATH, Locators.LOG_IN_MAIN_PAGE_BUTN).click()
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_LOGIN).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_PASS).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Locators.ENTER_BUTN).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.ORDER_BUTN)))
        assert len(driver.find_elements(By.XPATH, Locators.ORDER_BUTN)) == 1
# логин через лк
    def test_login_buttoon_lk(self, driver, wait):
        driver.get(Urls.OWN_SITE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LK_BUTN)))
        driver.find_element(By.XPATH, Locators.LK_BUTN).click()
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_LOGIN).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_PASS).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Locators.ENTER_BUTN).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.ORDER_BUTN)))
        assert len(driver.find_elements(By.XPATH, Locators.ORDER_BUTN)) == 1
# логин через кнопку на форме регистрации
    def test_login_registration_button(self, driver, wait):
        driver.get(Urls.REGISTER_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOGIN_REG_BUTN)))
        driver.find_element(By.XPATH, Locators.LOGIN_REG_BUTN).click()
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_LOGIN).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_PASS).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Locators.ENTER_BUTN).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.ORDER_BUTN)))
        assert len(driver.find_elements(By.XPATH, Locators.ORDER_BUTN)) == 1
# логин через кнопку на поле восстановлении пароля
    def test_login_recovery_button(self, driver, wait):
        driver.get(Urls.LOGIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.RECOVERY_BUTN)))
        driver.find_element(By.XPATH, Locators.RECOVERY_BUTN).click()
        driver.find_element(By.XPATH, Locators.LOGIN_REG_BUTN).click()
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_LOGIN).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_PASS).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Locators.ENTER_BUTN).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.ORDER_BUTN)))
        assert len(driver.find_elements(By.XPATH, Locators.ORDER_BUTN)) == 1

