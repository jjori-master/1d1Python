import unittest
from src.leetcode.medium.combination_sum import combination_sum


class CombinationSumTests(unittest.TestCase):
    def test_combination_sum(self):
        answer = combination_sum([2, 3, 6, 7], 7)

        self.assertListEqual(answer, [[2, 2, 3], [7]])


if __name__ == '__main__':
    unittest.main()
