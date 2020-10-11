def max_path(M):
    size = len(M)
    N = [[0 for _ in range(size)] for _ in range(size)]

    ### your code here ###

    return N[0][size-1]

### do not edit here ###
M = [[1,2,8,3],[0,4,3,6],[0,0,3,7],[0,0,0,2]]
print('최댓값 : ',max_path(M))