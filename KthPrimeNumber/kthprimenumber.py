import validate_prime

def kthprimeNumber(Number,position):
    primeNumber = []
    prime = Number
    if (validate_prime.isprime(Number)):
        prime = Number + 1
    while(len((primeNumber))!=position):
        if (validate_prime.isprime(prime)):
            primeNumber.append(prime)
        prime += 1
    return primeNumber[position-1]

print(kthprimeNumber(5,5))

