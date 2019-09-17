'''
https://www.hackerrank.com/challenges/py-if-else/problem
n 이 홀수면 Weird를 출력한다.
n 이 짝수고 2 부터 5사이의 숫자라면 Not Weird를 출력한다.
n 이 짝수고 6 부터 20사이의 숫자라면 Weird를 출력한다.
n 이 20보다 크다면 Not Weird를 출력한다.
'''


def is_odd(n):
    return n % 2 != 0


def if_else(n):
    # 홀수라면
    if is_odd(n):
        print("Weird")

    elif not is_odd(n) and 2 <= n <= 5:
        print("Not Weird")

    elif not is_odd(n) and 6 <= n <= 20:
        print("Weird")

    elif n > 20:
        print("Not Weird")

    return None
