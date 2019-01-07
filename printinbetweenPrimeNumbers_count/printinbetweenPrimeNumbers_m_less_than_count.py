import validate_prime

def inbetweenPrimeNumbers(m,n):
    if (m>n):
        return "Provide always M less than N"
    n = n + 1
    count = 0
    PrimeNumbers = []
    s = str("There is no Prime Numbers exsist")
    for i in range(m,n):
        if (validate_prime.isprime(i)):
            PrimeNumbers.append(i)
            count += 1
    if (m%2==0 and n%2==1 and len(PrimeNumbers)==2):
        return s
    elif (len(PrimeNumbers)==0 and count == 0):
        return s
    else:
        return PrimeNumbers,count
    return PrimeNumbers,count

print(inbetweenPrimeNumbers(2,3)) 