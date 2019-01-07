import math
def sumofdigits(N):
    sum = 0
    if (N < 0):
        return " Sorry,sum of digits of N can't be found"
    while(N!=0):
        temp = N % 10
        sum = sum + temp
        N = N / 10
    return math.floor(sum)
#print(math.floor(sumofdigits(-1234)))
print(sumofdigits(-10003))