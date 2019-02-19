Problem Statement :
===================    
    This function is to reverse a number
input :
=======
    Integer - Number 
Output :
========
    Reversed Number - Integer
Code :
=======    
def reversess(Number):
    reversedNumber = 0
    while (Number>0):
        temp = Number % 10
        reversedNumber = (reversedNumber*10)+temp
        Number = Number // 10
    return reversedNumber
