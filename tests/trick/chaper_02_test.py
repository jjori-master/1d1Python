from src.trick.chapter_02 import *

import unittest


class TestChapter02(unittest.TestCase):

    def test_apply_discount(self):
        shoes = {'name': 'Jo', 'price': 100}
        price = apply_discount(shoes, 0.25)

        assert price == 75

        with self.assertRaises(AssertionError):
            apply_discount(shoes, 2.0)
