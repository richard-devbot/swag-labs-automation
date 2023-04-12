from dsl import DSL

class Inventory_Page:
    def __init__(self, driver):
        self.dsl = DSL(driver)

    def get_inventory_items_titles(self):
        return self.dsl.get_items_titles("inventory_item_name")