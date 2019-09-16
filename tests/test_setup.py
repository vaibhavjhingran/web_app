import unittest
from selenium import webdriver


class TestSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://news.ycombinator.com/")
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()


