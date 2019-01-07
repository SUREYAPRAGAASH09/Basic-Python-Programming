import random
def Guess_the_Number(User):
    Secret_Number = random.randint(1,10)
    #print (Secret_Number)
    Attempt = 0
    while(User != Secret_Number):
        validation_Number = abs(User - Secret_Number)
        if ((validation_Number == 9 ) or (validation_Number == 8)):
            print("You are almost too far to that Number")
            print("And lesser than 5")
        elif ((validation_Number == 7) or (validation_Number == 6)):
            print("Your are far to that Number")
            print("And lesser than 5")
        #elif ((validation_Number == 5)):
        #    print("You have Guessed half of that Number")
        elif ((validation_Number == 4) or (validation_Number == 3)):
            print("You are almost nearer to that number")
            print("And Greater than 5")
        elif((validation_Number == 2) or (validation_Number == 1)):
            print("You are too nearer to that Number")
            print("And Greater than 5")
        
        #else:
         #   print("You are guessed the Number")
        User = int(input("Enter the Guessing Number"))
        Attempt += 1
    print("Finally You have Guessed the Number")
    print("And You have Guessed the Number in",end=" ") 
    print(Attempt,end=" ")
    print("attempts")

User = int(input("Enter the guessing Number"))
Guess_the_Number(User)