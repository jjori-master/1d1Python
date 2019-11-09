"""
문제 설명
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때,
전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 4 이상, 20이하인 문자열입니다.

입출력 예
phone_number	return
01033334444	    *******4444

javascript 풀이
function solution(phone_number) {
    return phone_number.split('').reverse().map((n, idx) => {
        if(idx < 4) {
            return n;
        }
        return '*';
    })
    .reverse()
    .join('')
}
"""


def hide_phone_number(phone_number):
    length = len(phone_number)
    return ''.ljust(length - 4, '*') + phone_number[length - 4:]


"""
문제 설명
1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면,
모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

1-1. 입력된 수가 짝수라면 2로 나눕니다.
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다.
위 작업을 몇 번이나 반복해야하는지 반환하는 함수, solution을 완성해 주세요.
단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

입출력 예 #2
16 -> 8 -> 4 -> 2 -> 1 이되어 총 4번만에 1이 됩니다.

입출력 예 #3
626331은 500번을 시도해도 1이 되지 못하므로 -1을 리턴해야합니다.
"""


def collatz_solution(num):
    answer = 0

    while num > 1 and answer < 500:
        if num % 2 == 0:
            num = int(num / 2)
            answer = answer + 1
            continue

        num = (num * 3) + 1
        answer = answer + 1

    return -1 if answer >= 500 else answer


"""
실패율
https://programmers.co.kr/learn/courses/30/lessons/42889
"""


def probability_of_failure(N, stages):
    answer = []

    for n in range(1, N + 1):
        total_count = len(stages)

        if not [x for x in stages if x == n]:
            answer.append([n, 0])
            continue

        stages = [x for x in stages if x > n]

        if not stages:
            answer.append([n, 1.0])
            continue

        answer.append([n, (total_count - len(stages)) / total_count])

    answer = [x[0] for x in sorted(answer, key=lambda e: (-e[1], e[0]))]

    return answer


"""
문자열 내 마음대로 정렬하기
https://programmers.co.kr/learn/courses/30/lessons/12915
"""


def sort_my_strings_at_will(strings, n):
    return sorted(strings, key=lambda s: (s[n], s))


"""
베스트앨범
https://programmers.co.kr/learn/courses/30/lessons/42579#
"""


def best_album(genres, plays):
    d = {}
    for idx, key in enumerate(genres):
        if key not in d:
            d[key] = {
                'total_count': 0,
                'members': {}
            }

        d[key]['total_count'] += plays[idx]
        d[key]['members'][idx] = plays[idx]

    keys = sorted(d, key=lambda k: d[k]['total_count'], reverse=True)

    answer = []
    for key in keys:
        target = d[key]
        members = target['members']

        top_members = sorted(members, key=lambda k: (-members[k], k))
        answer.extend(top_members[:2])

    return answer


def abuser(user_id, banned_id):
    answer = []

    for id in banned_id:
        target_idx = list(map(lambda l: l[0], (filter(lambda l: l[1], [[idx, s != '*'] for idx, s in enumerate(id)]))))
        target_str = id.replace('*', '')

        for uid in user_id:
            arr = [[idx, s] for idx, s in enumerate(uid)]
            v_uid = ''.join(map(lambda l: l[1], filter(lambda l: l[0] in target_idx, arr)))
            if target_str == v_uid and v_uid not in answer:
                answer.append(v_uid)

    return len(answer)


def rooms(k, room_number):
    hotel_rooms = dict.fromkeys([room_number for room_number in range(1, k+1)], False)
    answer = []

    for number in room_number:
        if not hotel_rooms[number]:
            hotel_rooms[number] = True
            print(hotel_rooms)
            answer.append(number)
            continue

        exists_room = False
        for p_number in range(number, k + 1):
            if not hotel_rooms[p_number]:
                hotel_rooms[p_number] = True
                answer.append(p_number)
                exists_room = True
                break

        if not exists_room:
            for p_number in range(1, k + 1):
                if not hotel_rooms[p_number]:
                    hotel_rooms[p_number] = True
                    answer.append(p_number)
                    break

    return answer
