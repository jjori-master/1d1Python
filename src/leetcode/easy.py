import math


# https://leetcode.com/problems/reverse-integer/
# 부호있는 32 비트 정수 'x'가 주어지면 숫자가 반전 된 'x'를 반환합니다.
# 'x'를 반대로하면 값이 부호있는 32 비트 정수 범위 [-2 ** 31, 2 ** 31-1]를
# 벗어나게되면 0을 반환합니다.

def reverse_integer(x: int) -> int:
    if x == 0:
        return 0

    sign = -1 if x < 0 else 1

    n = int(''.join(reversed(str(x * sign)))) * sign

    if n < -2147483648:
        return 0

    if n > 2147483647:
        return 0

    return n


# https://leetcode.com/problems/palindrome-number/
# Palindrome Number
def is_palindrome(x: int) -> bool:
    if len(str(x)) == 1:
        return True

    str_x = str(x)
    len_x = len(str_x)

    half_size = math.floor(len_x / 2)

    return str_x[0: half_size] == str_x[-half_size:][::-1]


# https://leetcode.com/problems/roman-to-integer/submissions/
# Roman to Integer
def roman_to_int(s: str) -> int:
    symbol_table = {
        'CM': 900,
        'CD': 400,
        'XC': 90,
        'XL': 40,
        'IX': 9,
        'IV': 4,
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total = []

    while len(s) > 0:
        for symbol in list(symbol_table):
            rs = s.replace(symbol, '', 1)
            if rs == s:
                continue

            total.append(symbol_table[symbol])
            s = rs
            break

    return sum(total)
