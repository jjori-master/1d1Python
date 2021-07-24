import unittest
from src.leetcode.easy.longest_common_prefix import longest_common_prefix


class LongestCommonPrefixTests(unittest.TestCase):
    def test_longest_common_prefix(self):
        strings = ["flower", "flow", "flight"]
        res = longest_common_prefix(strings)
        self.assertEqual(res, 'fl', '틀렸습니다.')

        strings = ["flower", "flower", "flower"]
        res = longest_common_prefix(strings)
        self.assertEqual(res, 'flower', '틀렸습니다.')


if __name__ == '__main__':
    unittest.main()
