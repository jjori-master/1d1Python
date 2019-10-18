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
