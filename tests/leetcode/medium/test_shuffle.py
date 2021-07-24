import unittest
from src.leetcode.medium.shuffle import shuffle


class ShuffleTests(unittest.TestCase):
    def test_shuffle(self):
        answer = shuffle([2, 5, 1, 3, 4, 7], 3)
        self.assertEqual(answer, [2, 3, 5, 4, 1, 7])

        answer = shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)
        self.assertEqual(answer, [1, 4, 2, 3, 3, 2, 4, 1])

        answer = shuffle([1, 1, 2, 2], 2)
        self.assertEqual(answer, [1, 2, 1, 2])


if __name__ == '__main__':
    unittest.main()
