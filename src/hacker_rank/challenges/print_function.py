'''
N이 3일 경우 123을 출력한다.
'''


def print_function(N):
    r = []
    for i in range(N):
        r.append(str(i + 1))
    print("".join(r))
