Problem :
    To count the no of digits given in a number
My Approach of giving Solution to the solution:
    step 1 : First define a Funtion named as "countnumbers"
        step 1.1 : In that, First initalize a variable named as count to Zero (to check how many digits are found in the given number after separation)
        step 1.2 : Then, Run a while loop untill we separate all the integers from the given number
            step 1.2.1 : initialize a "temp" variable and store the right most element of the digit
            step 1.2.2 : Then, increment the count variable by 1 untill the while get ends
            step 1.2.3 : store the remaining element of the digits after dividing it by 10 in a num and convert to int(num) (type conversio
Reason for using while loop :
                    I have used while loop instead of for loop because we could not make sure that when the number get ends                                                                                                          
 def countnumbers(num):
     count = 0
     while (num>0):
         temp = int(n) % 10
         count += 1
         num = int(num) / 10
         num = int(num)

     return count
