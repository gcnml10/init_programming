def simple_max_path(M):
    size = len(M)-1 

    ### your code here ###
    (i,j) = (0,size)
    sum_list = [M[0][size]]
    sum_ = 0
    for _ in range(0,size):
        if M[i][j-1] > M[i+1][j]:
            sum_list.append(M[i][j-1])
            (i, j) = (i,j-1)
        else:
            sum_list.append(M[i+1][j])
            (i, j) = (i + 1, j)
    sum_ = sum(sum_list)
    return sum_


### do not edit here ###
M = [[1,2,8,3],[0,4,3,6],[0,0,3,7],[0,0,0,2]]
print('최댓값 : ',simple_max_path(M))


