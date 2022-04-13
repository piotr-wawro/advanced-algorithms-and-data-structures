import unittest
from word.algorithms.anagram_in_text import anagram_in_text

class TestAnagramInText(unittest.TestCase):

    def test_text(self):
        word = 'light'
        self.assertEqual(anagram_in_text(word), ['light'])

if __name__ == '__main__':
    unittest.main()
