import validate_prime


def primeNumbersfrom2(N):
    PrimeNumbers = []
    if (N <= 1 or N ==2 ):
        return "Sorry,There is no Prime Numbers"
    for i in range(2,N):
        if validate_prime.isprime(i):
            PrimeNumbers.append(i) 
    return PrimeNumbers

print(primeNumbersfrom2(20))

#primeNumbersfrom2(0) 