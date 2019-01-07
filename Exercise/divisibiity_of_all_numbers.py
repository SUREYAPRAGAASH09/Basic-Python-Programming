#this function is used to check if all the digits of a number N is divisible by N
def divisibleofallNumbers(N):
    #sum = 0
    while(N>0):
        temp = N % 10
        if (N % temp == 0):
            N = N / 10
        else:
            return "the Number can't be divided"
    return "the Number can be divisible all the integers"

    
