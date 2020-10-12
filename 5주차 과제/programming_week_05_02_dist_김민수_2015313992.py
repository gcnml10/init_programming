def max_path(M):
    size = len(M)
    N = [[0 for _ in range(size)] for _ in range(size)]
    ### your code here ###
    for i in range(0,size):
        N[size-1-i][0] = sum(M[0][-1-i:])
        N[size-1][i] = sum([M[j][size-1] for j in range(0,i+1)])
    for i in range(1,size):
        for j in range(1,size):
            (x, y) = (size-i-1, j)
            if x >= y:
                N[x][y] = max(N[x][y-1],N[x+1][y]) + M[x][y]
            else:
                N[x][y] = max(N[x][y-1],N[x+1][y])
    return N[0][size-1]

### do not edit here ###
M = [[1,2,8,3],[0,4,3,6],[0,0,3,7],[0,0,0,2]]
print('최댓값 : ',max_path(M))