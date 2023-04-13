from dsl import DSL

class Inventory_Page:
    def __init__(self, driver):
        self.dsl = DSL(driver)

    def get_inventory_items_titles(self):
        return self.dsl.get_items_titles("inventory_item_name")
    
    def get_inventory_items_prices(self):
        return self.dsl.get_items_prices("inventory_item_price")
    
    def select_sort_type_by_text(self, visible_text_option):
        self.dsl.select_by_visible_text('//select[@data-test="product_sort_container"]', visible_text_option)

    def get_sort_type_text(self):
        return self.dsl.get_visible_text_selected('//select[@data-test="product_sort_container"]')