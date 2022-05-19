import unittest
from voting.algorithms.sainte_lague import sainte_lague

class TestSainteLague(unittest.TestCase):

    def test_case_1(self):
        party_votes = [742, 251, 987, 649]
        seats = 6

        self.assertListEqual(sainte_lague(party_votes, seats), [2,1,2,1])

if __name__ == '__main__':
    unittest.main()
