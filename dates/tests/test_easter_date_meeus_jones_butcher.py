import unittest
from dates.algorithms.easter_date_meeus_jones_butcher import easter_date_meeus_jones_butcher
from datetime import date

class TestEasterMeeusJonesButcher(unittest.TestCase):

    def test_case_1(self):
      self.assertEqual(easter_date_meeus_jones_butcher(2170), date(2170,4,1))

    def test_case_2(self):
      self.assertEqual(easter_date_meeus_jones_butcher(2049), date(2049,4,18))

    def test_case_3(self):
      self.assertEqual(easter_date_meeus_jones_butcher(2331), date(2331,3,29))

    def test_case_4(self):
      self.assertEqual(easter_date_meeus_jones_butcher(2020), date(2020,4,12))

    def test_case_5(self):
      self.assertEqual(easter_date_meeus_jones_butcher(2190), date(2190,4,25))

if __name__ == '__main__':
    unittest.main()
