import boot_Game
import input_file_boot_mode

#this function is used to iterate how many rounds do the player want to play
def count(rounds):
    #round = int(input("Enter how many rounds Do You want to play the game..\n Enter Here .."))    
    counti = 0
    while(counti < rounds):
        print ("\nThis is {0}".format(counti+1))
        input_file_boot_mode.get_names_from_user()
        counti += 1



#count(round)