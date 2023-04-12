from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

from login_page import Login_Page
from inventory_page import Inventory_Page

class Test_Product(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = Login_Page(self.driver)
        self.login_page.complete_login("standard_user", "secret_sauce")
        self.inventory_page = Inventory_Page(self.driver)

    def test_default_sort(self):
        items_titles = self.inventory_page.get_inventory_items_titles()
        sorted_items_titles = items_titles.copy()
        sorted_items_titles.sort()

        self.assertListEqual(items_titles, sorted_items_titles, "Items are not correctly ordered")



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
