import unittest
from tests.test_setup import TestSetup
from pages.loginpage import LoginPage
from test_data.user_details import UserDetails


class LoginTests(TestSetup):

    def test_login_user(self):
        login = LoginPage(self.driver)
        login.click_login()
        login.enter_username(UserDetails.USERNAME)
        login.enter_password(UserDetails.PASSWORD)
        self.save_screenshot()
        login.login_user()


if __name__ == '__main__':
    TestSetup.setUp()
    TestSetup.tearDown()
    unittest.main(verbosity=2)
