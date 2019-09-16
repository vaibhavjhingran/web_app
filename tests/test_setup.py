import unittest
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://news.ycombinator.com/")
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def wait_for(self, element, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
        except TimeoutException as e:
            print(e)
        finally:
            self.driver.quit()

    def save_screenshot(self):
        self.driver.save_screenshot('./screenshots/test-' + str(datetime.now()) + '.png')


