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
    answer =  probability_of_failure(5, [2, 1, 2, 6, 2, 4, 3, 3])
    assert answer == [3,4,2,1,5]

    answer = probability_of_failure(4, [4,4,4,4,4])
    assert answer == [4,1,2,3]
