import unittest
from word.algorithms.palindrome import palindrome

class TestPalindrome(unittest.TestCase):

    def test_word_even_1(self):
        word = 'asddsa'
        self.assertTrue(palindrome(word))

    def test_word_odd_1(self):
        word = 'asdsa'
        self.assertTrue(palindrome(word))

    def test_word_even_2(self):
        word = 'asdasd'
        self.assertFalse(palindrome(word))

    def test_word_odd_2(self):
        word = 'asdasda'
        self.assertFalse(palindrome(word))

    def test_word_short(self):
        word = 'as'
        self.assertFalse(palindrome(word))

if __name__ == '__main__':
    unittest.main()
