# coding=utf-8
def swap_case(str):
    swap_char_list = []
    for c in str:
        swap_char = c.isupper() and c.lower() or c.upper()
        swap_char_list.append(swap_char)

    return ''.join(swap_char_list)


'''https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen

Python has built-in string validation methods for basic data.
파이썬에는 기본 데이터에 대한 내장 문자열 유효성 검사 방법이 있습니다

It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
문자열이 알파벳 문자, 영숫자 문자, 숫자 등으로 구성되어 있는지 확인할 수 있습니다.

Task:
You are given a string S.
Your task is to find out if the string S contains:
alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
문자열에 영숫자, 영문자, 숫자, 소문자 및 대문자가 포함되어 있는지 확인해야합니다.

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
첫번째 줄은 S에 영숫문자가 존재할때 True 아닐때 False

In the second line, print True if  has any alphabetical characters. Otherwise, print False.
두번째 줄은 S에 문자가 있을 경우 True 아닐경우 False

In the third line, print True if  has any digits. Otherwise, print False.
세번째 줄은 S에 숫자가 있을 경우 True 아닐 경우 False

In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
네번째 줄은 소문자가 있을 경우 True 아닐 경우 False

In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
다섯째 줄은 대문자가 있을 경우 True 아닐 경우 False'''


def is_contains_alnum(S):
    for s in S:
        if s.isalnum():
            return True
    return False


def is_contains_alpha(S):
    for s in S:
        if s.isalpha():
            return True
    return False


def is_contains_digit(S):
    for s in S:
        if s.isdigit():
            return True
    return False


def is_contains_lower(S):
    for s in S:
        if s.islower():
            return True
    return False


def is_contains_upper(S):
    for s in S:
        if s.isupper():
            return True
    return False


def string_validators(S):
    print(is_contains_alnum(S))
    print(is_contains_alpha(S))
    print(is_contains_digit(S))
    print(is_contains_lower(S))
    print(is_contains_upper(S))
