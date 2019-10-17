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
