from collections import Counter
from functools import reduce
from itertools import combinations


# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
# 완주하지 못한 선수 문제 풀이
def incomplete_payers(participant, completion):
    participant = Counter(participant)
    for player_name in completion:
        target = participant[player_name] if player_name in participant else None

        if target is None:
            continue

        # 완주자라면 count를 하나 빼준다.
        participant[player_name] = target - 1 if target > 0 else 0

    return ','.join(list(map(lambda kv: kv[0], (filter(lambda kv: kv[1] > 0, participant.items())))))


# https://programmers.co.kr/learn/courses/30/lessons/42577
# 전화 번호
def phone_number_startswith(phone_book):
    answer = True

    for prefix_number in phone_book:
        res = {number for number in phone_book
               if number > prefix_number and number.startswith(prefix_number)}
        if not res:
            continue

        answer = False
        break

    return answer


# https://programmers.co.kr/learn/courses/30/lessons/42578
# 위장
def camouflage(clothes):
    li = list(dict(Counter(list(map(lambda c: c[1], clothes)))).values())

    answer = 0
    for i in range(len(li)):
        answer = answer + sum(list(map(lambda t: (reduce(lambda x, y: x * y, t)), list(combinations(li, i + 1)))))

    return answer
