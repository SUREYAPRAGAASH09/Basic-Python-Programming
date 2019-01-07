#                       this is the updated version of paper,scissors,rocks program

import paper_scissors_rock_program

#this function is used to iterate how many rounds do the player want to play
def count(rounds):
    counti = 0
    while(counti < rounds):
        print("This is",end=" ")
        print("round",end=" ")
        print(counti+1,end=" ")
        paper_scissors_rock_program.get_names_from_user()
        counti += 1


#round = int(input("Enter how many rounds Do You want to play the game..\n Enter Here .."))
#count(round)