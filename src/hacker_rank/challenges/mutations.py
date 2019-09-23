'''
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
Let's try to understand this with an example.
You are given an immutable string, and you want to make changes to it.

string = "abracadabra"
>>> print string[5]
a

string[5] = 'k'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

대충 해석하자면 list는 변경가능하고 tuples은 변경이 불가능 하다.
그래서 string의 index로 읽기는 가능하지만 쓰기는 불가능 하다.

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

해결 바안은 문자열을 리스트로 쪼갰다가 수정하고 다시 join하는 방법이 있다.

그래서 아무래도 문자열의 특정 인덱스 문자를 수정하는걸 해야 할듯
'''


def mutations(string, position, character):
    listed_string = list(string)
    listed_string[position] = character

    print(''.join(listed_string))
