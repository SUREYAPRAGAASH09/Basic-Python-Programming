import validate_prime
def prime_factors(N):
    #n = [2,3,5,7,11,13,19,23,29,31,]
    prime_numbers = []
    prime_factorss=[]
    M = N
    if (N<1 or N==0 or N==1):
        return "sorry prime Numbers can't be found"
    if (validate_prime.isprime(N)):
        M = M + 1
    for i in range(1,M):
        if (validate_prime.isprime(i)):
            prime_numbers.append(i)

    while (N!=1 or N!=1):
        for i in prime_numbers:
            if (N%i==0):
                prime_factorss.append(i)
                N = N/i

    return prime_factorss

print(prime_factors(-1))
