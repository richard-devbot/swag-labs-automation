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
        # xpath_index = '(//button[text()="Add to cart"])[' + str(index) + ']'
        # self.dsl.click_element_by_xpath(xpath_index)
        self.dsl.get_buttons_list_by_xpath('//button[text()="Add to cart"]')[index].click()
    
    def select_sort_type_by_text(self, visible_text_option):
        self.dsl.select_by_visible_text('//select[@data-test="product_sort_container"]', visible_text_option)

    def get_sort_type_text(self):
        return self.dsl.get_visible_text_selected('//select[@data-test="product_sort_container"]')
    
    def reset_app_state(self):
        self.dsl.click_element_by_id('react-burger-menu-btn')
        self.dsl.click_element_by_id('reset_sidebar_link')

    def access_cart(self):
        self.dsl.click_element_by_class('shopping_cart_link')