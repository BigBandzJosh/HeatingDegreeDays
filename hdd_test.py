import unittest
import HeatingDegreeDays

class TestHDD(unittest.TestCase):
      def testHDD1(self):
          self.assertEqual(HeatingDegreeDays.count_heating_degree_days([15, 18, 20, 25, 30, 35]), 1)

      def testHDD2(self):
          self.assertEqual(HeatingDegreeDays.count_heating_degree_days([15, 18, 20, 25, 3, 12]), 3)