from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

from login_page import Login_Page

class LoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = Login_Page(self.driver)

    def test_login_locked(self):
        self.login_page.set_login("locked_out_user")
        self.login_page.set_password("secret_sauce")
        self.login_page.click_login_button()

        self.assertEqual(
            self.driver.find_element(By.XPATH, '//h3[@data-test="error"]').text, 
            "Epic sadface: Sorry, this user has been locked out.",
            "Error message of locked user is incorrect."
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()