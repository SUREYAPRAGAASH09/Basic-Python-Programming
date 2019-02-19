Problem Statement :
===================
    To find the Armstrong Number 
Input :
=======
    Number - Integer
Output :
========
    Bool - True - If number is Armstrong Numeber
    Bool - False - If number is not a Armstrong Number
Code :
=======    
import count

def armstrongs(number):
    actualNumeber = number
    sum = 0
    flag = False
    count = count.countnumbers(number) 
    while (number > 0):
        temp = int(number) % 10
        temp = int(temp)
        sum = sum + (temp ** count)
        sum = int(sum)
        number = number / 10
        number = int(number)
    if (actualNumber == sum):
        flag = True
    return flag
