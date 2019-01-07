#this function is used to check whether the given number is prime or not
#01-01-2019
import math
def isprime(n):
    Flag = True
    if (n==1 ):
        return False
        
    if(n<=0):
        return False
        
    if (n==2):
        return True
        
    for i in range(2,int(math.sqrt(n)+1)):
        if (n%i==0):
            Flag = False
        
    return Flag

#n = int(input("Enter the integer"))
#print(isprime(n))
