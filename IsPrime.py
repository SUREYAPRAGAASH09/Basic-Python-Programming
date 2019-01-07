#to Check given number is prime or not
import math 
def Isprime(N):
    #Flag = True
    #print N
    if(N <= 0):
        return False  
    if(N==1 ):
        return False  
    for i in range(2,int(math.sqrt(N)+1)): #change in while loop  
        if (N%i == 0):
            return False
        else:
            return True
    #return Flag



#N = int(input("Enter the number"))
#(primenumbers(N))
print (Isprime(3))