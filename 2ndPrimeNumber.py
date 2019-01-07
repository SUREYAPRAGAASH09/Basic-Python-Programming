import IsPrime

def printSecondPrimeNUmber(N):
    count = 0
    i = N
    while(count < 2):
        if (IsPrime.Isprime(i)):
            print (i)
            i = i + 1
            
            count = count + 1
        i = i + 1
        #count = count + 1
    #print b

(printSecondPrimeNUmber(2))