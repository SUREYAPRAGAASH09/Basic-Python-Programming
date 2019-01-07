#check the status 
# This function is used to check who is the winner and the losser from the two players 
#def check_status(1stplayers_choice,2ndplayers_choice):
 #   #count = 0
 #   flag = False
 #   if (("Paper" == P) or ("Rock" == R) or ("scissors" == S)):
 #       return Fals
 #  else:
 #       return True

def check_status_machine(p1,p2):
    flag = True
    if(p1 == p2):
        flag = False
    return flag

def check_status_two_players(p1,p2):
    p1 = p1.lower()
    p2 = p2.lower()
    if p1 == p2 :
        print ("the match gets draw")
    else:

        b = list(p1)
        v = list(p2)
        ni = b[0]+v[0]
    
        if (("rs" == ni) or ("pr" == ni) or ("ps" == ni) or ("sp" == ni)):
            print("Player 1 is the winner")
        else:
            print("Player 2 is the winner")

  
#p1 = str(input("Enter the choice 1"))
#p2 = str(input("Enter the choice 2"))
#print (c) 

#def counter_Engine(p1,p2):
    #count = 0
    #if (check_status(p1,p2)):
  #      count = count + 1
 #   return count
p1 = str(input("Enter the choice 1"))
p2 = str(input("Enter the choice 2"))
(check_status_two_players(p1,p2)) 
