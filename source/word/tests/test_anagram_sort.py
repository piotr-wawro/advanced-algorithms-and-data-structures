import unittest
from word.algorithms.anagram_sort import anagram_sort

class TestAnagramSort(unittest.TestCase):

    def test_anagram(self):
        text1 = 'I am lord voldemort'
        text2 = 'Tom marvolo riddle'

        self.assertTrue(anagram_sort(text1, text2))

if __name__ == '__main__':
    unittest.main()
