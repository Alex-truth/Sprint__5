from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators import Locators
from urls import Urls
from data import Data

class TestDesignerSection:
    # перехд к разделу булок
    def test_bread_section(self, driver, wait):
        driver.get(Urls.OWN_SITE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BREAD_BUTN)))
        driver.find_element(By.XPATH, Locators.SAUCE_BUTN).click()
        driver.find_element(By.XPATH, Locators.BREAD_BUTN).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.BREAD_BUTN)))
        current_class = driver.find_element(By.XPATH, Locators.BREAD_BUTN).get_attribute('class')
        assert Locators.ACTIVE_CLASS in current_class
    # переход к разделу соусов
    def test_sauce_section(self, driver, wait):
        driver.get(Urls.OWN_SITE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.SAUCE_BUTN)))
        driver.find_element(By.XPATH, Locators.SAUCE_BUTN).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.SAUCE_BUTN)))
        current_class = driver.find_element(By.XPATH, Locators.SAUCE_BUTN).get_attribute('class')
        assert Locators.ACTIVE_CLASS in current_class
    # переход к разделу начинки
    def test_filling_section(self, driver, wait):
        driver.get(Urls.OWN_SITE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.FILLING_BUTN)))
        driver.find_element(By.XPATH, Locators.FILLING_BUTN).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.FILLING_BUTN)))
        current_class = driver.find_element(By.XPATH, Locators.FILLING_BUTN).get_attribute('class')
        assert Locators.ACTIVE_CLASS in current_class
