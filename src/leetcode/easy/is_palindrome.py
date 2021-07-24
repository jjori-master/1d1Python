import math


# https://leetcode.com/problems/palindrome-number/
# Palindrome Number
def is_palindrome(x: int) -> bool:
    if len(str(x)) == 1:
        return True

    str_x = str(x)
    len_x = len(str_x)

    half_size = math.floor(len_x / 2)

    return str_x[0: half_size] == str_x[-half_size:][::-1]
