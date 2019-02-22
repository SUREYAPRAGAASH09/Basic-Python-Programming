Problem Statement :
==================== 
      To count the no of digits given in a number
Input :
========  
   Integer 
Output :
=========
    Count all the integers - integer 
Code :
======= 
 def countnumbers(n): 
     count = 0
     while (n>0):
         temp = int(n) % 10
         count += 1
         n = int(n) / 10
         n = int(n)
     return count
Another Method :
=================      
#another variant of solving the above problem
def countnumbers(num):
    n = list(str(num))
    n = len(num)
    return num
    

#print(countnumbers(1234512345))
