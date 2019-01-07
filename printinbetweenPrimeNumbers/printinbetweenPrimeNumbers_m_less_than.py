import validate_prime

def inbetweenPrimeNumbers(m,n):
    if (m>n):
        return "Provide always M less than N"
    n = n + 1
    #if (m==1 and n==2):
     #   n += 1
    PrimeNumbers = []
    s = str("There is no Prime Numbers exsist")
    
    for i in range(m,n):
        if (validate_prime.isprime(i)):
            PrimeNumbers.append(i)
    
    if (m%2==0 and n%2==1 and len(PrimeNumbers)==2):
        return s
    else:
        return PrimeNumbers
    
    #if (m%2==1 and n%2==1 and len(PrimeNumbers)==1):
    #    return s
    #else:
    return PrimeNumbers

    
    #if (m%2==0 and n%2==0 and len(PrimeNumbers)==0):
    #    return s
    #lse:
    #   return PrimeNumbers
    #print(len(PrimeNumbers))
    
    

print(inbetweenPrimeNumbers(3,2)) 