from src.programmers.data_types import *


def test_remove_mating():
    r = remove_mating('cbcb')
    assert r == 0

    r = remove_mating('bbcc')
    assert r == 1

    r = remove_mating('baabaa')
    assert r == 1
