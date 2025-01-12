from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators import Locators
from urls import Urls
from data import Data

class TestSwichLkDesigner:
# переход на страницу ЛК по клику на "Личный кабинет"
    def test_swich_lk(self, driver, wait):
        driver.get(Urls.LOGIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.INPUT_AUTH_LOGIN)))
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_LOGIN).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_PASS).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Locators.ENTER_BUTN).click()
        driver.find_element(By.XPATH, Locators.LK_BUTN).click()
        wait.until(expected_conditions.url_to_be(Urls.PROFILE_PAGE))
        assert driver.current_url == Urls.PROFILE_PAGE
# переход со страницы ЛК на страницу коструктора по клику на «Конструктор»
    def test_swich_lk_designer(self, driver, wait):
        driver.get(Urls.LOGIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.INPUT_AUTH_LOGIN)))
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_LOGIN).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_PASS).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Locators.ENTER_BUTN).click()
        driver.find_element(By.XPATH, Locators.LK_BUTN).click()
        wait.until(expected_conditions.url_to_be(Urls.PROFILE_PAGE))
        driver.find_element(By.XPATH, Locators.DESIGNER_BUTN).click()
        wait.until(expected_conditions.url_to_be(Urls.OWN_SITE))
        assert driver.current_url == Urls.OWN_SITE
# перехд со страницы ЛК на страницу конструктора по клику на логотип Stellar Burgers
    def test_swich_lk_logo_Burgers(self, driver, wait):
        driver.get(Urls.LOGIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.INPUT_AUTH_LOGIN)))
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_LOGIN).send_keys(Data.EMAIL)
        driver.find_element(By.XPATH, Locators.INPUT_AUTH_PASS).send_keys(Data.PASSWORD)
        driver.find_element(By.XPATH, Locators.ENTER_BUTN).click()
        driver.find_element(By.XPATH, Locators.LK_BUTN).click()
        wait.until(expected_conditions.url_to_be(Urls.PROFILE_PAGE))
        driver.find_element(By.XPATH, Locators.LOGO_BURGERS).click()
        wait.until(expected_conditions.url_to_be(Urls.OWN_SITE))
        assert driver.current_url == Urls.OWN_SITE

