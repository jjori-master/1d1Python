'''
https://www.hackerrank.com/challenges/python-tuples/problem

Task를 단순 해석하자면, integer 숫자로 이뤄진 리스트를 tuple로 만들고 그 tuple을 이용하여
hash값을 뽑아내라.

'''


def tuples_and_hash(strings):
    integer_list = map(int, strings.split())
    t = tuple(integer_list)
    return hash(t)
