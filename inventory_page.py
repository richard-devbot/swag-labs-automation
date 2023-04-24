from dsl import DSL

class Inventory_Page:
    def __init__(self, driver):
        self.dsl = DSL(driver)

    def get_inventory_items_titles(self):
        return self.dsl.get_items_titles("inventory_item_name")
    
    def get_inventory_item_title_by_index(self, index):
        return self.dsl.get_items_titles("inventory_item_name")[index]
    
    def get_inventory_items_prices(self):
        return self.dsl.get_items_prices("inventory_item_price")
    
    def get_inventory_item_price_by_index(self, index):
        return self.dsl.get_items_prices("inventory_item_price")[index]
    
    def add_item_to_cart_by_index(self, index):
        self.dsl.get_buttons_list_by_xpath('//div[@class="inventory_item"]//button')[index].click()
    
    def select_sort_type_by_text(self, visible_text_option):
        self.dsl.select_by_visible_text('//select[@data-test="product_sort_container"]', visible_text_option)

    def get_sort_type_text(self):
        return self.dsl.get_visible_text_selected('//select[@data-test="product_sort_container"]')
    
    def reset_app_state(self):
        self.dsl.click_element_by_id('react-burger-menu-btn')
        self.dsl.click_element_by_id('reset_sidebar_link')
        self.dsl.click_element_by_id('react-burger-cross-btn')

    def access_cart(self):
        self.dsl.click_element_by_class('shopping_cart_link')

    def go_to_checkout(self):
        self.dsl.click_element_by_xpath('//button[@id="checkout"]')

    # checkout
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