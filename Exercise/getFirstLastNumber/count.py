To count the no of digits given in a number
 def countnumbers(n): 
     count = 0
     while (n>0):
         temp = int(n) % 10
         count += 1
         n = int(n) / 10
         n = int(n)

     return count
another variant of solving the above problem
def countnumbers(n):
    n = list(str(n))
    n = len(n)
    return n
    

#print(countnumbers(1234512345))
