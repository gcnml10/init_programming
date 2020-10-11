def score_average():
    """
    - 평균 성적 구하기
    - 반복문을 사용하여 성적을 입력 받는다.
    - 'q' 입력시 종료
    - 조건문을 이용해 입력한 성적이 숫자가 아닌 경우('q' 제외) 오류 메세지는 출력하고 다시 성적을 입력 받는다.
    - 받을 수 있는 성적의 범위를 벗어난 경우 오류 메세지는 출력하고 다시 성적을 입력 받는다.

    """
    ######### 함수 완성하기 #########

import math

sum = 0
count = 0
while True:
    num = input('점수(0~100) : ')
    if num == 'q':
        break
    try:
        int(num)
    except:
        print('%형식 오류%')
        continue
    if not 0 <= int(num) <= 100:
        print('%범위 오류%')
        continue
    num = int(num)
    sum += num
    count += 1
average = sum / count

print(str(count) + ' 과목 평균 성적: ' + str(round(average,1)))

######### ######### #########


# 수정 금지
score_average()
