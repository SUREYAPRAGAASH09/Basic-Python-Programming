Problem Statement :
===================
    To check whether the given number is palindrome or not 
Input :
=======
    Number - Integer
Output :
========
    Flag - True if palindrome exsist - Boolean
    Flag - False if palindrome does Not exsist - Boolean
Code :
=======
import reverse
def palindrome(Number):
    actualNum  = Number
    reversedNumber = reverse.reversess(N) 
    flag = False
    if actualNum == reversedNumber:
        flag = True
    return flag
