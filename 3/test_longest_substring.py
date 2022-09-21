import unittest
from longest_substring import longest_substring


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_empty_string(self) -> None:
        self.assertEqual(0, longest_substring(''))

    def test_one_char(self) -> None:
        self.assertEqual(1, longest_substring('a'))

    def test_two_different_chars(self) -> None:
        self.assertEqual(2, longest_substring('a1'))

    def test_two_same_chars(self) -> None:
        self.assertEqual(1, longest_substring('aa'))

    def test_longest_first(self) -> None:
        self.assertEqual(2, longest_substring('aba'))
        self.assertEqual(3, longest_substring('ab1b$'))

    def test_longest_last(self) -> None:
        self.assertEqual(2, longest_substring('aab'))
        self.assertEqual(5, longest_substring('ab1b$ 2'))

    def test_longest_middle(self) -> None:
        self.assertEqual(5, longest_substring('a bac;b'))

    def test_examples(self) -> None:
        self.assertEqual(3, longest_substring('abcabcbb'))
        self.assertEqual(1, longest_substring('bbbbb'))
        self.assertEqual(3, longest_substring('pwwkew'))


if __name__ == '__main__':
    unittest.main()
