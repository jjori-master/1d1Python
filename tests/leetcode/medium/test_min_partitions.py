import unittest
from src.leetcode.medium.min_partitions import min_partitions


class MinPartitionsTests(unittest.TestCase):
    def test_min_partitions(self):
        answer = min_partitions('32')
        self.assertEqual(answer, 3)

        answer = min_partitions('82734')
        self.assertEqual(answer, 8)

        answer = min_partitions('27346209830709182346')
        self.assertEqual(answer, 9)


if __name__ == '__main__':
    unittest.main()
