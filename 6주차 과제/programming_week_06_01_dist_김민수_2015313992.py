class Grade:
    # 클래스를 완성하세요.
    """
    - def __init__(name: str, : grade_list: List(int) = int)
    - def __len__( ) -> len(grade_list) : 점수 리스트 길이 리턴
    - def get_average() -> float :평균 점수 리턴
    """

    def __init__(self, name: str, grade_list: list):
        self.name = name
        self.grade_list = grade_list
    #
    # def __len__(self):
    #     return self.grade_list.__len__() # len(self.grade_list)
    #
    # def __str__(self):
    #     return self.grade_list

    def __len1__(self):
        return len(self.grade_list)    ##이건 왜 안되는 건지

    def get_average(self):
        list_sum = sum(self.grade_list)
        average = list_sum/len(self.grade_list)
        return float(average)


###### do not edit here #######
p = Grade("박융합",[45,66,93])
# print("{0}의 {1}과목 평균 점수: {2}".format(p.name, len(p) ,p.get_average()))

### 질문: len()와 __len__()의 차이?
# print(p.grade_list.__len__())
# print(len(p))####
# print(p.__len__())
print(p.__len1__())

#
# print(len(p.grade_list))
#
# print(p.__str__())
# print(len(p.__str__()))
