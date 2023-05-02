from dsl.dsl import DSL

import re

class Checkout_Page:
    def __init__(self, driver):
        self.dsl = DSL(driver)
    
    def set_first_name(self, first_name):
        self.dsl.insert_text_by_id('first-name', first_name)

    def set_last_name(self, last_name):
        self.dsl.insert_text_by_id('last-name', last_name)

    def set_zip_postal_code(self, zip_postal_code):
        self.dsl.insert_text_by_id('postal-code', zip_postal_code)

    def continue_to_checkout_overview(self):
        self.dsl.click_element_by_id('continue')

    def fulfill_checkout_informantion(self, first_name, last_name, zip_postal_code):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_zip_postal_code(zip_postal_code)
        self.continue_to_checkout_overview()

    def continue_to_checkout_overview(self):
        self.dsl.click_element_by_id('continue')

    def get_total_value(self):
        text_n_value = self.dsl.get_text_by_class('summary_subtotal_label')
        value = float( re.search(r'\d+\.\d+', text_n_value).group() )
        return value
    
    def finish_overview(self):
        self.dsl.click_element_by_id('finish')

    def get_checkout_status_message(self):
        self.dsl.get_text_by_class('title')

    def get_checkout_complete_message(self):
        self.dsl.get_text_by_class('complete-header')