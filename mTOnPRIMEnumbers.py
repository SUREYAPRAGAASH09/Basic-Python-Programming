
import math
def isprime(N):
    flag = True
    if (N <= 0 or N == 1):
        return False
    for i in range(2,int(math.sqrt(N)+1)):
        if (N%i==0):
            return False
    return flag

def inbe(m,n):
    for i in range(m,n):
        if (isprime(i)):
            print (i) 

#inbe(10,1)
m = int(input("enter the 1st numbers    "))
n = int(input("enter the 2nd numbers    "))
if (m<n):
    inbe(n,m)
else:
    inbe(m,n)
#print m,n
#print isprime(2)