import validate_prime

#n = int(input("Enter the number"))
#print(validate_prime.isprime(n))

def prime_numbers_from_1_to_N(N):
    primeNumbers = [1]
    #print ("1")
    N = abs(N)
    for i in range(2,N-1):
        if (validate_prime.isprime(i)):
            primeNumbers.append(i)
            #print (i)
    return primeNumbers

#prime_numbers_from_1_to_N(50)
print(prime_numbers_from_1_to_N(2))