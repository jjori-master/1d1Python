'''
 문자열 S가 주어졌을때 공백으로  split 하고 하이픈(-)으로 join 한다.
'''


def strings_split_and_join(S):
    splited_str = S.split(' ')
    joined_str = '-'.join(splited_str)
    print(joined_str)
