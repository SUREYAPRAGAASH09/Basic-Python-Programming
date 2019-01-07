import count

def armstrongs(n):
    num = n
    sum = 0
    flag = False
    counti = count.countnumbers(n) 
    while (n > 0):
        temp = int(n) % 10
        temp = int(temp)
        sum = sum + (temp ** counti)
        sum = int(sum)
        n = n / 10
        n = int(n)
    if (num == sum):
        flag = True
    return flag

print(armstrongs(153))
