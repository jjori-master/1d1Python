from src.leetcode.medium import *


def test_min_partitions():
    answer = min_partitions('32')
    assert answer == 3

    answer = min_partitions('82734')
    assert answer == 8

    answer = min_partitions('27346209830709182346')
    assert answer == 9


def test_shuffle():
    answer = shuffle([2, 5, 1, 3, 4, 7], 3)
    assert answer == [2, 3, 5, 4, 1, 7]

    answer = shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)
    assert answer == [1, 4, 2, 3, 3, 2, 4, 1]

    answer = shuffle([1, 1, 2, 2], 2)
    assert answer == [1, 2, 1, 2]
