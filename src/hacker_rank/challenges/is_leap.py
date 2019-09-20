'''
윤년(leap year)구하기

In the Gregorian calendar three criteria must be taken into account to identify leap years:
그레고리력에서 윤년을 식별하려면 다음 세 가지 기준을 고려해야합니다.

The year can be evenly divided by 4, is a leap year, unless:
연도를 4로 나눌수 있다면 윤년입니다. 그렇지 않으면

The year can be evenly divided by 100, it is NOT a leap year, unless
연도를 100으로 균등하게 나눌 수 있다면, 윤년이 아닙니다. 그렇지 않으면

The year is also evenly divisible by 400. Then it is a leap year.
연도는 400으로 균등하게 나눌 수 있다면, 윤년입니다.

'''


def is_leap(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True
    return False
