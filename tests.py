import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome('C:\\Users\\mykeltuz\\Downloads\\Programs\\chromedriver') # change this path to run this test on your device.

class WebpageTests(unittest.TestCase):

    def test_title(self):
        """ Check page title """
        driver.get(file_uri("stoplight.html"))
        self.assertEqual(driver.title, "Stoplight")

    def test_red(self):
        """ Check red light """
        driver.get(file_uri("stoplight.html"))
        red = driver.find_element_by_id("red")
        red.click()
        self.assertEqual(red.value_of_css_property("fill"), "rgb(255, 0, 0)")

    def test_yellow(self):
        """ Check blue light """
        driver.get(file_uri("stoplight.html"))
        yellow = driver.find_element_by_id("yellow")
        yellow.click()
        self.assertEqual(yellow.value_of_css_property("fill"), "rgb(255, 255, 0)")
    
    def test_green(self):
        """ Check green light """
        driver.get(file_uri("stoplight.html"))
        green = driver.find_element_by_id("green")
        green.click()
        self.assertEqual(green.value_of_css_property("fill"), "rgb(0, 128, 0)") 
    

if __name__ == "__main__":
    unittest.main()