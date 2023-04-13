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

    @unittest.skip('')
    def test_default_sort(self):
        items_titles = self.inventory_page.get_inventory_items_titles()
        sorted_items_titles = items_titles.copy()
        sorted_items_titles.sort()

        self.assertEqual(self.inventory_page.get_sort_type_text(), 'Name (A to Z)', 'Default order is not correct.')
        self.assertListEqual(items_titles, sorted_items_titles, "Items are not correctly ordered.")

    @unittest.skip('')
    def test_invert_named_sort(self):
        self.inventory_page.select_sort_type_by_text('Name (Z to A)')
        
        items_titles = self.inventory_page.get_inventory_items_titles()
        reverse_sorted_items_titles = items_titles.copy()
        reverse_sorted_items_titles.sort()
        reverse_sorted_items_titles.reverse()

        self.assertListEqual(items_titles, reverse_sorted_items_titles, "Items are not correctly ordered.")
        self.assertEqual(self.inventory_page.get_sort_type_text(), 'Name (Z to A)', 'Selected order is not correct.')

    def test_sort_price_low_high(self):
        self.inventory_page.select_sort_type_by_text('Price (low to high)')

        items_prices = self.inventory_page.get_inventory_items_prices()
        sorted_items_prices = items_prices.copy()
        sorted_items_prices.sort()

        self.assertEqual(self.inventory_page.get_sort_type_text(), 'Price (low  high)', 'Order is not the selected one.')
        self.assertListEqual(items_prices, sorted_items_prices, "Items are not correctly ordered by price (low to high).")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
