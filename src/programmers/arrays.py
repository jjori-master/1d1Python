from itertools import permutations


# https://programmers.co.kr/learn/courses/30/lessons/42748
# 위장
def k_number(array, commands):
    answer = []

    for c in commands:
        s = c[0] - 1
        e = c[1]
        t = c[2]

        dab = sorted(array[s:e])[t - 1: t]

        answer.append(dab[0])

    return answer


def big_number(numbers):
    return max(map(lambda l: ''.join(l), permutations(str(n) for n in numbers)))
