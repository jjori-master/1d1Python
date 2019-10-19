from src.programmers.hash import *


def test_incomplete_payers():
    participant = ['leo', 'kiki', 'eden']
    completion = ['eden', 'kiki']

    assert incomplete_payers(participant, completion) == 'leo'

    participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
    completion = ['josipa', 'filipa', 'marina', 'nikola']

    assert incomplete_payers(participant, completion) == 'vinko'

    participant = ['mislav', 'stanko', 'mislav', 'ana']
    completion = ['stanko', 'ana', 'mislav']

    assert incomplete_payers(participant, completion) == 'mislav'


def test_phone_number_startswith():
    answer = phone_number_startswith(['119', '97674223', '1195524421'])
    assert not answer

    answer = phone_number_startswith(['123', '456', '789'])
    assert answer

    answer = phone_number_startswith(['12', '123', '1235', '567', '88'])
    assert not answer
