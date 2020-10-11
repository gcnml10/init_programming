### write funtion 'sumrange_tail()'

# sumrange_tail()
# - type: (tail recursion) function
# - input : two numbers
# - ouput : sum of all numbers between two numbers (two numbers also included)
# - tail recursion: do not assign sum results during recursion


def sumrange_tail(m, n):
    ### your code here ####
    return loop(m, n, 0)


def loop(m, n, sum):
    if m <= n:
        return loop(m+1,n,sum+m)
    else:
        return sum



### do not edit here ###
print('합:', sumrange_tail(3, 7))
