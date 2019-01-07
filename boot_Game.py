#                                                   Boot Game      
#                            this program is updated version of paper,scissors,rock program
#def generate_random_number():
    
import os
#this function is used to check the condition ie the core logic of the program
def Test(player_1_choice,player_2_choice):
        concatennated_user_input = player_1_choice + player_2_choice
        if (player_1_choice == player_2_choice):
            return "Match_Draw"
        elif (("rs" == concatennated_user_input) or ("pr" == concatennated_user_input) or ("ps" == concatennated_user_input) or ("sp" == concatennated_user_input)):
            return "Player_1"    
        else:
            return "Player_2"
        