from src.programmers.problem_solving_learning import *


def test_hide_phone_number():
    number = hide_phone_number('01033334444')
    assert number == '*******4444'

    number = hide_phone_number('0103334443')
    assert number == '******4443'
