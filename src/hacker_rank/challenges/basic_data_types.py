def lists(list, command):
    splited_command = command.split(' ')
    c = splited_command[0]

    if c == 'print':
        print(list)
        return

    method_to_call = getattr(list, c)

    if len(splited_command) > 2:
        position = int(splited_command[1])
        value = int(splited_command[2])

        method_to_call(position, value)
        return

    if len(splited_command) > 1:
        value = int(splited_command[1])

        method_to_call(value)
        return

    method_to_call()


# 두번째로 낮은 점수를 가지고 있는 학생 이름을 출력
def nested_lists(li):
    scores = list(set(map(lambda i: i[1], li)))
    scores.sort()
    second_score = scores[1]

    def match_second_score(info):
        return second_score == info[1]

    second_score_list = list(filter(match_second_score, li))
    second_score_names = list(set(map(lambda i: i[0], second_score_list)))
    second_score_names.sort()

    for name in second_score_names:
        print(name)
