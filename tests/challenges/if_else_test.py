'''
https://www.hackerrank.com/challenges/py-if-else/problem
n 이 홀수면 Weird를 출력한다.
n 이 짝수고 2 부터 5사이의 숫자라면 Not Weird를 출력한다.
n 이 짝수고 6 부터 20사이의 숫자라면 Weird를 출력한다.
n 이 20보다 크다면 Not Weird를 출력한다.
'''

from src.hacker_rank.challenges.if_else import if_else


def test_if_else(capsys):
    if_else(1)
    captured = capsys.readouterr()
    assert captured.out == "Weird\n"

    if_else(2)
    captured = capsys.readouterr()
    assert captured.out == "Not Weird\n"

    if_else(4)
    captured = capsys.readouterr()
    assert captured.out == "Not Weird\n"

    if_else(6)
    captured = capsys.readouterr()
    assert captured.out == "Weird\n"

    if_else(20)
    captured = capsys.readouterr()
    assert captured.out == "Weird\n"

    if_else(22)
    captured = capsys.readouterr()
    assert captured.out == "Not Weird\n"
