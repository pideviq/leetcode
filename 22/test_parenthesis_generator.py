import unittest
from parenthesis_generator import parenthesis_generator


class TestParenthesisGenerator(unittest.TestCase):
    def test_empty(self) -> None:
        self.assertEqual([''], parenthesis_generator(0))

    def test_n_is_one(self) -> None:
        self.assertEqual(['()'], parenthesis_generator(1))

    def test_n_is_two(self) -> None:
        self.assertEqual(['(())', '()()'], parenthesis_generator(2))

    def test_n_is_three(self) -> None:
        self.assertEqual(['((()))', '(()())', '(())()', '()(())', '()()()'],
                         parenthesis_generator(3))


if __name__ == '__main__':
    unittest.main()
