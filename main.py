import csv
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.LoginPage import LoginPage
from pages.TakeSnapShot import TakeSnapShot


class PythonOrgSearch(unittest.TestCase):
    """Simple data mining solution"""

    # Setup chrome
    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        # options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path='/home/rifat/chromedriver')
        self.driver.get("http://agency.bk.toprankon.com/")

    # start seach in medex
    def test_search_in_medex(self):
        snap = TakeSnapShot(self.driver)
        snap.take_snap('2', 'agency.bk.toprankon.com')

    # driver down
    def tearDown(self):
        # self.driver.close()
        pass


if __name__ == "__main__":
    unittest.main()
