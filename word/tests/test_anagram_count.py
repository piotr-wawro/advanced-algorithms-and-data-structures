import unittest
from word.algorithms.anagram_count import anagram_count

class TestAnagramCount(unittest.TestCase):

    def test_anagram(self):
        text1 = 'I am lord voldemort'
        text2 = 'Tom marvolo riddle'

        self.assertTrue(anagram_count(text1, text2))

if __name__ == '__main__':
    unittest.main()
