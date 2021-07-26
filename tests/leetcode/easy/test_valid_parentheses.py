import unittest
from src.leetcode.easy.valid_parentheses import valid_parentheses


class ValidParenthesesTests(unittest.TestCase):
    def test_valid_parentheses(self):
        s = "()"
        answer = valid_parentheses(s)
        self.assertTrue(answer)

        s = "()[]{}"
        answer = valid_parentheses(s)
        self.assertTrue(answer)

        s = "(]"
        answer = valid_parentheses(s)
        self.assertFalse(answer)

        s = "([)]"
        answer = valid_parentheses(s)
        self.assertFalse(answer)

        s = "{[]}"
        answer = valid_parentheses(s)
        self.assertTrue(answer)


if __name__ == '__main__':
    unittest.main()
