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


def test_camouflage():
    clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
    answer = camouflage(clothes)

    assert answer == 5

    clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]
    answer = camouflage(clothes)

    assert answer == 3

    clothes = [['얼굴1', '얼굴'], ['얼굴2', '얼굴'], ['얼굴3', '얼굴'],  ['상의1', '상의'],  ['상의2', '상의'], ['하의', '하의']]
    answer = camouflage(clothes)

    assert answer == 23


