import unittest
from voting.algorithms.hondt import hondt

class TestHondt(unittest.TestCase):

    def test_case_1(self):
        party_votes = [742, 251, 987, 649]
        seats = 6

        self.assertListEqual(hondt(party_votes, seats), [2,0,3,1])

if __name__ == '__main__':
    unittest.main()
