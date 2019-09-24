'''
In this challenge, the user enters a string and a substring.
이 도전에서 유저는 문자열과 부분문자열을 입력합니다.

You have to print the number of times that the substring occurs in the given string.
주어진 문자열에서 부분 문자열이 발생하는 횟수를 인쇄해야합니다.

String traversal will take place from left to right, not from right to left.
문자열 순회는 오른쪽에서 외쪽으로가 아닌 왼쪽에서 오른쪽으로 진행된다.

input:
ABCDCDC
CDC

output:
2
'''


def find_a_string(string, sub_string):
    N = len(string) - len(sub_string) + 1
    match_count = 0

    for i in range(N):
        if string[i:(i + len(sub_string))] == sub_string:
            match_count += 1
    return match_count
