#Printing the inbetween Prime Numbers
import math
def Isprime(N):
    Flag = True
    if (N<=0 or N == 1):
        return False
    for i in range(2,int(math.sqrt(N)+1)):
        if (N%i == 0):
            return False
    return Flag

def inbetween_Prime_Numbers(M,N):

    #N = N + 1
    for i in range(N,M):
        if Isprime(i):
            print (i)

M = int(input("Enter the 1st Nuber"))
N = int(input("Enter the 2nd Number"))
if (M<N) :
    inbetween_Prime_Numbers(N,M)
else:
    inbetween_Prime_Numbers(M,N)
