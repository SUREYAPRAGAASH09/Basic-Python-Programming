Problem Statement :
===================    
      to get First and last number from the given number
Input :
=======
    Number - Integer 
Output :
=======
    Get first integer and last integer - integer 
Code :
=====    
import count
def gettingFirstLastNumber(num): 
    check = 10
    check_1 = check
    check_first = 1
    for i in range(1,count.countnumber(n)):
        check_first = check * check_first
    first =  n / check_first
    last = n % check_1
    return int(first),int(last)

 
