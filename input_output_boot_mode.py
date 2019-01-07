#this is input file for the boot mode program
import random
import boot_Game
#this is fucntion is used to validate user input 
def validate_user_input(user_input):
    valid_inputs = ['s','r','p']
    user_input = user_input.lower()
    if (user_input in valid_inputs):
        return user_input
    else:
        get_input()

#this function is used to get the input from the user
def get_input():
    print("Enter any one from this list play the game \nPaper for p \nRock for r\nScissors for s ")
    player_1_choice = str(input("Enter your Choice here ..  "))
    player_1_choice = validate_user_input(player_1_choice)
    random_integer = random.randint(0,2)
    valid_inputs = ['s','r','p']
    player_2_choice = valid_inputs[random_integer]
    output(player_1_choice,player_2_choice)

def output(player_1_choice,player_2_choice):
    check = boot_Game.Test(player_1_choice,player_2_choice)
    if (check == "Match_Draw"):
        print("Match Draw")
    elif (check == "Player_1"):
        print("Player 1 is the winner")
    else:
        print("Player 2 is the winner")
