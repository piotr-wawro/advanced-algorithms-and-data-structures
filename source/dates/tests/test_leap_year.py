import unittest
from dates.algorithms.leap_year import is_leap_year
from datetime import date

class TestLeapYear(unittest.TestCase):

    def test_case_1(self):
      self.assertTrue(is_leap_year(2020))

    def test_case_2(self):
      self.assertFalse(is_leap_year(2700))

    def test_case_3(self):
      self.assertFalse(is_leap_year(2251))

    def test_case_4(self):
      self.assertTrue(is_leap_year(3200))

if __name__ == '__main__':
    unittest.main()
