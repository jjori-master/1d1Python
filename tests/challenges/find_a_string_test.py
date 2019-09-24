from src.hacker_rank.challenges.find_a_string import find_a_string


def test_find_a_string():
    match_count = find_a_string('ABCDCDC', 'CDC')
    assert match_count == 2
