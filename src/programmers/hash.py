from collections import Counter


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
    pass
