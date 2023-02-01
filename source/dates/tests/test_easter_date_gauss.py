import unittest
from dates.algorithms.easter_date_gauss import easter_date_gauss
from datetime import date

class TestEasterDateGauss(unittest.TestCase):

    def test_case_1(self):
      self.assertEqual(easter_date_gauss(2170), date(2170,4,1))

    def test_case_2(self):
      self.assertEqual(easter_date_gauss(2049), date(2049,4,18))

    def test_case_3(self):
      self.assertEqual(easter_date_gauss(2331), date(2331,3,29))

    def test_case_4(self):
      self.assertEqual(easter_date_gauss(2020), date(2020,4,12))

    def test_case_5(self):
      self.assertEqual(easter_date_gauss(2190), date(2190,4,25))

if __name__ == '__main__':
    unittest.main()
