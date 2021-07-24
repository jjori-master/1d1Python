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
