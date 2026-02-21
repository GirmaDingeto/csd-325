# test_cities.py
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for the function city_country.py"""

    def testcity_country(self):
        """Do values like 'Santiago, Chile' work correctly?"""
        formatted_string = city_country("Santiago", "Chile")
        self.assertEqual(formatted_string, "Santiago, Chile")

if __name__ == '__main__':

    unittest.main()