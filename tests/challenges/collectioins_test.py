from src.hacker_rank.challenges.collections import *


def test_shoes_shop():
    number_of_shoes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
    customer_needs = ['6 55', '6 45', '6 55', '4 40', '18 60']
    result = shoes_shop(number_of_shoes, customer_needs)

    assert result == 200


def test_calc_deque(capsys):
    operations = ['append 1', 'append 2', 'append 3', 'appendleft 4', 'pop', 'popleft']

    result = deque_operator(operations)
    list = []
    for n in result:
        list.append(n)

    print(list)
    captured = capsys.readouterr()

    assert captured.out == '[1, 2]\n'
