import os

#this function is used to check whether input entered by the user is correct or not.
# if the user input is in the  list of words then the word are tken into account
# otherwise it prompt the user to enter the correct input to the fuction 
def validate_user_input(user_input,first_players_name,second_players_name):
    valid_inputs = ['s','r','p']
    user_input = user_input.lower()
    user_input_letter_separation = list(user_input)
    if (user_input_letter_separation[0] in valid_inputs):
        return user_input_letter_separation[0]
    else:
        get_user_input(first_players_name,second_players_name)

#this function is used to get the name from the user for interactiveness. 
def get_names_from_user():
    first_players_name = str(input("\nEnter 1st players delightful Name .. "))
    second_players_name = str(input("\nEnter 2nd players delightful Name .. "))
    get_user_input(first_players_name,second_players_name)

#this function is used to get the input from the user
def get_user_input(first_players_name,second_players_name):
    print("\nEnter any one of the following in the list avaiable below inorder to play the game \n1.Paper\n2.Rock\n3.Scissors ")
    print(first_players_name,end=" ")
    player_1_choice = str(input("\nEnter any one of the item avaiable from the list.Please Enter your Choice here ..  "))
    player_1_choice = validate_user_input(player_1_choice,first_players_name,second_players_name)
    os.system("CLS")
    print("\nEnter any one of the following in the list avaiable below inorder to play the game \n1.Paper\n2.Rock\n3.Scissors ")
    print(second_players_name)
    player_2_choice = str(input("\nEnter any one of the item avaiable from the list \n Please Enter your choice here .. "))
    player_2_choice = validate_user_input(player_2_choice,first_players_name,second_players_name)
    Test(player_1_choice,player_2_choice,first_players_name,second_players_name)

#this function is used to check the condition ie the core logic of the program
def Test(player_1_choice,player_2_choice,first_players_name,second_players_name):
    concatennated_user_input = player_1_choice + player_2_choice
    if (player_1_choice == player_2_choice):#THIS CONDITION IS USED CHECK IF BOTH INPUT STRING IS SAME THEN PRINT MATCH DRAW
        print ("\nthe match gets draw")
    elif (("rs" == concatennated_user_input) or ("pr" == concatennated_user_input) or ("ps" == concatennated_user_input) or ("sp" == concatennated_user_input)):
            print(first_players_name,end=" ")
            print("is the winner \n" )
            print(second_players_name,end=" ")
            print("is the runner in this match")
            #player1_count_value += 1
    else:
        print(second_players_name,end=" ")
        print("is the winner \n")
        print(first_players_name,end=" ")
        print("is the runner in this match")
        #player2_count_value +=1

#get_names_from_user()