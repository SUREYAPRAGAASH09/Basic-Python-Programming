import math
def digital_root(N):
    sum = 0
    while (sum > 9 or N > 0):
        if N == 0:
            N = sum
            sum = 0
        
        temp = math.floor(N) % 10
        sum = math.floor(sum) + temp
        N = math.floor(N) / 10
    return sum

print(digital_root(12345)) 
