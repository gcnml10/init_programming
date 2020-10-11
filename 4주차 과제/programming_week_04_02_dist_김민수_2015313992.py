def binary_search(arr, score):
    ### 초기값 설정
    ### do not edit here ###
    low = 0
    high = len(arr)
    arr = sorted(arr)

    ### 코드를 작성하세요
    while low<=high:
        mid = (high + low)//2
        if score == arr[mid]:
            return mid
        elif score < arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return rank


# 파일 불러오기 코드 작성
# scores_str : List[str]
t = open("scores.txt","r")
scores_str = t.readlines()
t.close()
### do not edit here ###
scores = [float(score) for score in scores_str]
my_score = 81
rank = binary_search(scores, my_score)
print(f'{my_score}은 {rank}등 입니다')