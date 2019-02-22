Problem Statement :
===================    
    to find count the number of odd and even number in a given integer
Input :
=======
    Integer Number 
Output :
========
    Even Count and Odd Count - Integer
Code :
======    
def countevenodd(number):
    even = 0
    odd = 0
    while(number>0):
        temp = number % 10
        if (temp%2==0):
            even += 1
        else:
            odd += 1
        number = number / 10
            return even,odd

        
