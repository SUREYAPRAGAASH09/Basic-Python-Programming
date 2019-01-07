#to get First and last number from the given number
import count
def gettingFirstLastNumber(n): 
    counti = count.countnumbers(n)
    counti = counti 
    check = 10
    check_1 = check
    check_first = 1
    for i in range(1,counti):
        check_first = check * check_first
    first =  n / check_first
    last = n % check_1
    return int(first),int(last)

print(gettingFirstLastNumber(123456789))   
