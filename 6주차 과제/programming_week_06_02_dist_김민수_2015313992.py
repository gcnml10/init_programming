import random

class Account:
    # 클래스를 완성하세요
    
    """
    -	보안문제로 외부에서 내부의 정보를 수정할 수 없도록 변수를 설정해야함
    -	계좌번호와 잔고의 경우 표시된 결과와 다를 수 있음
    -	def __init__(name: str, birthday: str)
    -	def __str__() -> 계좌정보
    -	def deposit(amount:int) :입금 함수
    -	def withdraw(amount:int) 출금 함수
    -	필요시 random() 함수 사용 가능
    -	안전코딩 : 입금은 0원 미만일 수 없고, 출금은 잔고 이상일 수 없음
    """
    def __init__(self, name: str, birthday: str):
        self.__name = name
        self.__birthday = birthday
        self.__account = str(random.randint(0,999)).zfill(3) + "-" + str(random.randint(0,99)).zfill(2) + "-" + str(random.randint(0,999999)).zfill(6)
        self.__balance = random.randint(0,1000)

    def __str__(self):
        return "이름: {}\n생년월일: {}\n계좌번호: {}\n잔고: {}".format(self.__name, self.__birthday,self.__account,self.__balance,)

    def show_balance(self):
        return print("잔고: {}".format(self.__balance))

    def deposit(self, amount:int):
        if amount >0 :
            self.__balance = self.__balance + amount
            return print("{}원 입금".format(amount))
        else:
            return print("입금불가")

    def withdraw(self, amount:int):
        if 0 < amount <= self.__balance:
            self.__balance = self.__balance - amount
            return print("{}원 출금".format(amount))
        else:
            print('출금불가')

###### do not edit here ####### 
person = Account("김성균", "990218")
print(person)
print("#####")
person.deposit(100)
person.deposit(-1)
person.show_balance()
person.withdraw(500)
person.withdraw(0)
person.show_balance()