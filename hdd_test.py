import unittest
from HeatingDegreeDays import Temperature, count_heating_degree_days

class TestHDD(unittest.TestCase):
    def testHDD1(self):
        # Create Temperature objects with values in Celsius
        temperatures = [Temperature(15), Temperature(18), Temperature(20), Temperature(25), Temperature(30), Temperature(35)]
        self.assertEqual(count_heating_degree_days(temperatures), 1)

    def testHDD2(self):
        # Create Temperature objects with values in Celsius
        temperatures = [Temperature(15), Temperature(18), Temperature(20), Temperature(25), Temperature(3), Temperature(12)]
        self.assertEqual(count_heating_degree_days(temperatures), 3)
