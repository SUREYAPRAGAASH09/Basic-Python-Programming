Problem Statement :
===================    
    this function is used to check if all the digits of a number N is divisible by N
Input :
=======
    Integer 
Output :
========
    Flag - Bool
Code :
=======    
def divisibleofallNumbers(Num):
    flag = False 
    while(Num>0):
        temp = Num % 10
        if (Num % temp == 0):
            flag = True
        num = num / 10
    return  flag  


