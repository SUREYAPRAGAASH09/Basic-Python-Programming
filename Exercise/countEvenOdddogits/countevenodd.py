#to find count the number of odd and even number in a given integer
def countevenodd(n):
    even = 0
    odd = 0
    while(n>0):
        temp = int(n) % 10
        if (temp%2==0):
            even += 1
        else:
            odd += 1
        n = int(n) / 10
        n = int(n)
    return even,odd

print(countevenodd(12345))
