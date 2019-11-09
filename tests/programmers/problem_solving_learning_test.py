from src.programmers.problem_solving_learning import *


def test_hide_phone_number():
    number = hide_phone_number('01033334444')
    assert number == '*******4444'

    number = hide_phone_number('0103334443')
    assert number == '******4443'


def test_collatz_solution():
    answer = collatz_solution(6)
    assert answer == 8

    answer = collatz_solution(16)
    assert answer == 4

    answer = collatz_solution(626331)
    assert answer == -1


def test_probability_of_failure():
    answer = probability_of_failure(5, [2, 1, 2, 6, 2, 4, 3, 3])
    assert answer == [3, 4, 2, 1, 5]

    answer = probability_of_failure(4, [4, 4, 4, 4, 4])
    assert answer == [4, 1, 2, 3]


def sort_my_strings_at_will():
    answer = sort_my_strings_at_will(['sun', 'bed', 'car'], 1)
    assert answer == ['car', 'bed', 'sun']

    answer = sort_my_strings_at_will(['abce', 'abcd', 'cdx'], 1)
    assert answer == ['abcd', 'abce', 'cdx']


def best_album_test():
    answer = best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
    assert answer == [4, 1, 3, 0]

    answer = best_album(["classic", "pop", "classic", "classic", "pop"], [200, 600, 200, 100, 2500])
    assert answer == [4, 1, 0, 2]

    answer = best_album(["classic", "pop", "classic", "classic"], [200, 5000, 200, 100])
    assert answer == [1, 0, 2]

    answer = best_album(["classic", "pop", "classic", "classic", "pop"], [200, 100, 200, 100])
    assert answer == [0, 2, 1]

def test_abuser():
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]

    answer = abuser(user_id, banned_id)
    assert answer == 2

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["*rodo", "*rodo", "******"]

    answer = abuser(user_id, banned_id)
    assert answer == 2

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]

    answer = abuser(user_id, banned_id)
    assert answer == 3

def test_rooms():
    k = 10
    room_number = [1, 3, 4, 1, 3, 1]
    answer = rooms(k, room_number)
    assert answer == [1, 3, 4, 2, 5, 6]
