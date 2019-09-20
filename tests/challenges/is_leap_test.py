from src.hacker_rank.challenges.is_leap import is_leap


def test_is_leap():
    res = is_leap(1990)
    assert not res

    res = is_leap(1800)
    assert not res

    res = is_leap(2100)
    assert not res

    res = is_leap(2000)
    assert res

    res = is_leap(2400)
    assert res
