import unittest
from voting.algorithms.hare_niemeyer import hare_niemeyer

class TestHareNiemeyer(unittest.TestCase):

    def test_case_1(self):
        party_votes = [742, 251, 987, 649]
        seats = 6

        self.assertListEqual(hare_niemeyer(party_votes, seats), [2,1,2,1])

if __name__ == '__main__':
    unittest.main()
