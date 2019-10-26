from src.programmers.arrays import *


def test_k_number():
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    answer = k_number(array, commands)

    assert answer == [5, 6, 3]
