from selenium import webdriver
from selenium.webdriver.common.by import By

class DSL:
    def __init__(self, driver):
        self.driver = driver

    def insert_text_by_id(self, id_locator, text):
        self.driver.find_element(By.ID, id_locator).send_keys(text)

    def click_element_by_id(self, id_locator):
        self.driver.find_element(By.ID, id_locator).click()