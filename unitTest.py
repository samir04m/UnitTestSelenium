import time
import unittest
from selenium import webdriver

class pruebaUnitaria(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        url = "https://refugio-animales.herokuapp.com/"
        self.driver.get(url)
        time.sleep(3)

    def test_registro(self):
        self.driver.find_element_by_id("registro").click()
        


    def tearDown(self)
        self.driver.quit()
