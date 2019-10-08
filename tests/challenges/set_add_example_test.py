from src.hacker_rank.challenges.set import *


def test_set_add_example():
    s = set()
    list = ['UK', 'China', 'USA', 'France', 'New Zealand', 'UK', 'France']

    for name in list:
        set_add_example(s, name)

    assert len(s) == 5
