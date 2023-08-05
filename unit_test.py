"""
This unit test for making sure the data in the database is up to date and not missing
any divisions. Also tests whether the server is up and running.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By

API_SERVER_ADDR = "http://127.0.0.1:8000"

chrome_driver_path = Service(
    "/home/camcamyoung125/Professional_Portfolio_Projects/chromedriver-linux64/chromedriver")

xpath = "/html/body/pre"
list_divisions = [
    "heavyweight",
    "lightheavyweight",
    "middleweight",
    "welterweight",
    "lightweight",
    "featherweight",
    "bantamweight",
    "flyweight",
    "wfeatherweight",
    "wbantamweight",
    "wflyweight",
    "wstrawweight",
    "watomweight"
]


class TestClass(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = webdriver.Chrome(service=chrome_driver_path)
            self.driver.get(API_SERVER_ADDR)
        except WebDriverException:
            print(" Server not running")

    def test_data_by_division(self):
        for weight in list_divisions:
            self.driver.get(f"{API_SERVER_ADDR}/division/{weight}")
            try:
                text = self.driver.find_element(By.XPATH, xpath)
                if len(text.text) > 20:
                    assert True
                else:
                    print(f"{weight} division not in database please update")
                    assert False
            except NoSuchElementException as err:
                print(err)
                assert False

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
