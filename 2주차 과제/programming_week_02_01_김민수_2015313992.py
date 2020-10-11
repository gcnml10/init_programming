
def isleapyear(year):
 """
- 윤년 계산하기
- return : Boolean expression

"""
######### 함수 완성하기 #########
 year = int(year);
 boolean = False
 if year % 4 == 0:
     if year % 100 != 0:
         boolean = True
     elif year % 400 == 0:
         boolean = True
     else:
         boolean = False
 else:
     boolean = False

 return boolean

######### ######### #########


# 수정 금지
while True:
    year = input("연도: ")
    if year == 'q':
        break
        
    print(isleapyear(int(year)))