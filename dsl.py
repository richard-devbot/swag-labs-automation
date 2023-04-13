from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DSL:
    def __init__(self, driver):
        self.driver = driver

    def insert_text_by_id(self, id_locator, text):
        self.driver.find_element(By.ID, id_locator).send_keys(text)

    def click_element_by_id(self, id_locator):
        self.driver.find_element(By.ID, id_locator).click()

    # Inventory page
    def get_items_titles(self, class_locator):
        items_titles = []
        for item_title in self.driver.find_elements(By.CLASS_NAME, class_locator):
            items_titles.append(item_title.text)
        return items_titles
    
    def get_items_prices(self, class_locator):
        items_prices = []
        for item_price in self.driver.find_elements(By.CLASS_NAME, class_locator):
            only_numbers = item_price.text.replace('$', '')
            items_prices.append(float(only_numbers))
        return items_prices
    
    def select_by_visible_text(self, xpath_locator, visible_text):
        select = Select(self.driver.find_element(By.XPATH, xpath_locator))
        select.select_by_visible_text(visible_text)

    def get_visible_text_selected(self, xpath_locator):
        select = Select(self.driver.find_element(By.XPATH, xpath_locator))
        return select.first_selected_option.text