'''
철수 국어 90, 수학 70, 영어 50
영희 국어 10, 수학 10, 영어 20

일때 철수 또는 영희의 평균 값 구하기

소수점 자릿수는 2자리로 맞춤
'''

student_marks = {'Harsh': [25, 26.5, 28], 'Krishna': [67, 68, 69]}


def finding_the_percentage(name):
    scores = student_marks[name]

    total_score = 0
    for score in scores:
        total_score += score

    avg = round(total_score / len(scores), 2)
    print("{0:.2f}".format(avg))
