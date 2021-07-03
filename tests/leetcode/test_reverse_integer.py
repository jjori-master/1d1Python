from src.leetcode.easy import reverse_integer


def test_reverse_integer():
    answer = reverse_integer(123)
    assert answer == 321

    answer = reverse_integer(-123)
    assert answer == -321

    answer = reverse_integer(120)
    assert answer == 21

    answer = reverse_integer(0)
    assert answer == 0
