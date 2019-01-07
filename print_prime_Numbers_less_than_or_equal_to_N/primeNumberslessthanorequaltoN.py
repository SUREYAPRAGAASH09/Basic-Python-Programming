import validate_prime

def printNumberlessthanorequaltoN(N):
    count = 0
    Prime = 2
    PrimeNumbers = []
    while (count<N):
        if(validate_prime.isprime(Prime)):
            PrimeNumbers.append(Prime)
        count = len(PrimeNumbers)   
        Prime+=1
        #count += 1
    return PrimeNumbers

#print(printNumberlessthanorequaltoN() )