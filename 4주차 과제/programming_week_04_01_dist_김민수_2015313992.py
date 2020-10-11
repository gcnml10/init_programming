def ATM_min_wait(N, nums):
    # return : min_sum 
    # 사람 당 현금 인출 시 소요되는 누적시간의 총합의 최솟값
    
    # 사람이 1명인 경우
    if N == 1:
        # 코드를 작성하세요
        min_sum = 1*nums[0]
        return min_sum

    # 사람이 2명 이상인 경우 
    else :
        # 코드를 작성하세요
        # 1. 가장 적은 시간이 드는 순서로 줄서기 : bubble sort 사용
        # 2. 1번 데이터를 이용해 min_sum 구하기
        data = nums
        sorted_data = []
        while data:
            large = data[0]
            for i in range(len(data) - 1):
                if data[i] > data[i + 1]:
                    large = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = large
                else:
                    large = data[i + 1]
            sorted_data.insert(0, large)
            data.remove(large)
        min_sum = 0
        for i in range(0, N):
            min_sum += (N - i) * sorted_data[i]
        return min_sum

### do not edit here ###
print('최소 시간:', ATM_min_wait(1, [5]))
print('최소 시간:', ATM_min_wait(5, [3, 1, 4, 3, 2]))