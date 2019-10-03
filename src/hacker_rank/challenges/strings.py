# coding=utf-8
import textwrap


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


'''
https://www.hackerrank.com/challenges/python-string-formatting/problem
Given an integer, N, print the following values for each integer i from 1 to n :
정수 N이 주어지면 1부턴 n까지 각 정수 i에 대해 다음 값을 인쇄하십시오.. 싫어..
1. Decimal 10진수
2. Octal 8진수
3. Hexadecimal (capitalized) 16진수 대문자 표시해라잉
4. Binary 2진수

The four values must be printed on a single line in the order specified above for each i from 1 to n.
네 개의 값은 1에서 n까지의 각 i에 대해 위에서 지정한 순서대로 한 줄에 인쇄되어야합니다.

Each value should be space-padded to match the width of the binary value of n.
각 값은 n의 이진 값 너비와 일치하도록 공백으로 채워야합니다.
N이 17일 경우 2진수는 10001 즉 5칸으로 채우면된다.
'''


def interval(N, target):
    length = len(bin(N)[2:]) - len(str(target)) + 1
    return ''.join([' '] * (length + 1))


def string_formatting(N):
    for i in range(N):
        n = i + 1
        dec = n
        octal = int(oct(n), 8)
        hexadecimal = format(n, 'x').upper()
        binary = bin(n)[2:]

        str = f'{dec} {octal} {hexadecimal} {binary}'

        print(str)


'''
You are given a string S and width w.
너에게 S라는 문자와 w라는 길이를 제공한다.

You task is to wrap the string into a paragraph of width w.
너의 일은 문자열을 w 너비의 단락으로 감싸는 것

textwrap 라이브러리 사용
'''


def wrap(string, max_width):
    print('\n'.join(textwrap.wrap(string, max_width)))


def capitalize(s):
    arr = s.split(' ')
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()

    print(' '.join(arr))
