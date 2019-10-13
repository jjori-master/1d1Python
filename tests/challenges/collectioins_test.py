from src.hacker_rank.challenges.collections import *
from collections import deque


def test_shoes_shop():
    number_of_shoes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
    customer_needs = ['6 55', '6 45', '6 55', '4 40', '18 60']
    result = shoes_shop(number_of_shoes, customer_needs)

    assert result == 200

'''
list를 공백으로 출력할 경우 *을 붙여서 출력한다.
L = [1, 2]
print(*L)
>>> 1 2

공백 외에 다른 문자로 구분하여 출력할 경우  sep를 옵션으로 제공한다.
L = [1, 2]
print(*L, sep=', ')
>>> 1, 2

print(*L, sep=' -> ')
>>> 1 -> 2
'''
def test_calc_deque(capsys):
    input_commands = ['append 1', 'append 2', 'append 3', 'appendleft 4', 'pop', 'popleft']

    d = deque()
    for command in input_commands:
        operate_deque(d, command)

    print(*list(d))
    captured = capsys.readouterr()

    assert captured.out == '1 2\n'
