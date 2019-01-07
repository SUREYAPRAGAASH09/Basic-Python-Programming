#To find out all factor of  “N” –numbers.
def factor(n):
    factors = []
    n  =abs(n)
    if (n==1):
        return 1
    for i in range(2,n):
        if (n%i==0):
            factors.append(i)
    return factors
#print (factor(4))
print(factor(3))
