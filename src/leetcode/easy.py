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
