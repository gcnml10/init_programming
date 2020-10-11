data = [32,23,18,7,11,99,55]
sorted_data = []

# def bubble(s):
#     def loop(s,ss,sss):
#         if len(s)>1:
#             if s[0]>s[1]:
#                 return loop(s[1],s[0]+s[2:],sss)
#             else:
#                 return loop(ss[1:],ss+[0],sss)
#         else:
#             return loop(s,ss,s+sss)
#     return loop(s,[],[])

def ATM_min_wait(N: int, nums: list) -> int:
    data = nums
    sorted_data = []
    while data:
        large = data[0]
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                large = data[i]
                data[i] = data[i+1]
                data[i+1] = large
            else:
                large = data[i+1]
        sorted_data.insert(0, large)
        data.remove(large)
    sum = 0
    for i in range(0, N):
        sum += (N-i)*sorted_data[i]
    return sum
print('최소 시간:', ATM_min_wait(1, [5]))
print('최소 시간:', ATM_min_wait(5, [3, 1, 4, 3, 2]))