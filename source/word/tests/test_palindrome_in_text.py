import unittest
from word.algorithms.palindrome_in_text import palindrome_in_text

class TestPalindromeInText(unittest.TestCase):

    def test_text_1(self):
        text = 'shukaku'
        self.assertListEqual(
            palindrome_in_text(text),
            [
                'ukaku',
                'kak',
            ]
        )

    def test_text_2(self):
        text = 'aa'
        self.assertListEqual(
            palindrome_in_text(text),
            [
                'aa',
            ]
        )

if __name__ == '__main__':
    unittest.main()
