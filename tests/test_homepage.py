import unittest
from pages.homepage import HomePage
from tests.test_setup import TestSetup


class HomePageTests(TestSetup):

    def test_homepage_icon(self):
        home_icon = HomePage(self.driver)
        home_icon.click_home_icon()
        home_icon.assert_title()

    def test_all_header_links(self):
        headers = HomePage(self.driver)
        headers.click_all_header_links()


if __name__ == '__main__':
    TestSetup.setUp()
    TestSetup.tearDown()
    unittest.main(verbosity=2)

