from element_locators.loginpage_elements import LoginElements


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        login = self.driver.find_element_by_css_selector(LoginElements.login_link_css)
        login.click()

    def enter_username(self, username):
        user = self.driver.find_element_by_css_selector(LoginElements.username_field_css)
        user.clear()
        user.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element_by_css_selector(LoginElements.password_field_css)
        password_field.clear()
        password_field.send_keys(password)

    def login_user(self):
        login_button = self.driver.find_element_by_css_selector(LoginElements.login_btn_css)
        login_button.click()