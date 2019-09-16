import unittest
from selenium import webdriver


class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://news.ycombinator.com")
        self.driver.implicitly_wait(5)

    def test_homepage_icon(self):
        driver = self.driver
        driver.find_element_by_css_selector("a[href$='news']").click()
        assert 'Hacker News' in driver.title

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
