import unittest
from src.leetcode.easy.reverse_integer import reverse_integer


class ReverseIntegerTests(unittest.TestCase):
    def test_reverse_integer(self):
        answer = reverse_integer(123)
        self.assertEqual(answer, 321)

        answer = reverse_integer(-123)
        self.assertEqual(answer, -321)

        answer = reverse_integer(120)
        self.assertEqual(answer, 21)

        answer = reverse_integer(0)
        self.assertEqual(answer, 0)


if __name__ == '__main__':
    unittest.main()
