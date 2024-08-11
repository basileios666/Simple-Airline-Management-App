import os
import pathlib
import unittest
from selenium import webdriver
# Create your tests here.

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):
    
    def test_title(self):
        driver.get(file_uri("index.html"))
        self.assertEqual(driver.title, ("Flights"))
        
        
if __name__ == "__mail__":
    unittest.main()