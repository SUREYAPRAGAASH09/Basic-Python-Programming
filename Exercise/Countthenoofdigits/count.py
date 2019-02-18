Problem Statemnts :
===================
    To count the no of digits given in a number
    
Input :
=======
    Integer 
Output :
========
    Count Value - Integer  
    
Reason for using while loop :
==============================
                    I have used while loop instead of for loop because we could not make sure that when the number get ends                                                                                                          
Code :
======    
    def countnumbers(number):
     count = 0
     while (number>0):
         temp = int(number) % 10
         count += 1
         num = int(number) / 10
         num = int(number)
     return count
