from dsl.dsl import DSL

class Login_Page:
    def __init__(self, driver):
        self.dsl = DSL(driver)

    def set_login(self, username):
        self.dsl.insert_text_by_id("user-name", username)

    def set_password(self, password):
        self.dsl.insert_text_by_id("password", password)

    def click_login_button(self):
        self.dsl.click_element_by_id("login-button")

    def complete_login(self, username, password):
        self.dsl.insert_text_by_id("user-name", username)
        self.dsl.insert_text_by_id("password", password)
        self.dsl.click_element_by_id("login-button")