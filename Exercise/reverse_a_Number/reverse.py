#this function is to reverse a number

def reversess(N):
    rev_num = 0
    while (N>0):
        temp = N % 10
        rev_num = (rev_num*10)+temp
        N = N // 10
    return rev_num-1

print(reversess(1234))


