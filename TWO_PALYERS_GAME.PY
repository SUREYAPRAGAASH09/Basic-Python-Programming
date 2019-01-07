#THIS FUNCTION IS USED TO CHECK WHO IS THE WINNER 
#PSEUDOCODE
    #STEP 1.THE TWO INPUT STRING IS CONVERTED INTO LOWER CASE
    #STEP 2.CHECK IF BOTH THE INPUT STRING IS SAME OR NOT. IF SAME PRINT THE MATCH GETS DRAW
    #STEP 3.IF NOT, SEPARATE THE LETTERS FROM THE STRING AND CONCATENATE THE FISRT CHARACTER OF THE TWO INPUT STRING AND THE CONCATENTATION OF TWO FIRST CHARACTER IS STORED IN VARIABLE "NI"
     
    #STEP 4:COMPARING WITH VARIABLE NI WITH STRING "RS" WHERE RS MEANS ROCK, SCISSORS AND 
    #                               NI WITH STRING "PR" WHERE PR MEANS PAPER,ROCK AND
    #                               NI WITH STRING "PS" WHERE PS MEANS PAPER STONE AND
    #                               NI WITH STRING "SP" WHERE SP MEANS SCISSORS,PAPERS 
    #               IF ANY OF THE CONDITION SATISFIES THEN PRINT PLAYER 1 IS THE WINNER 
    #   ELSE PRINT PLAYER 2 IS THE WINNER 
def check_status_two_players(player1choice,player2choice):
    player1choice = player1choice.lower()#THIS IS USED TO CONVERT THE STRING TO LOWER CASE 
    player2choice = player2choice.lower()#THIS IS USED TO CONVERT THE STRING TO LOWER CASE
    

    if player1choice == player2choice :#THIS CONDITION IS USED CHECK IF BOTH INPUT STRING IS SAME THEN PRINT MATCH DRAW
        print ("the match gets draw")
    else:

        player1choice_first_character = list(player1choice)#THIS METHOD USED TO SEPARATE THE LETTER BY LETTER
        player1choice_second_character = list(player2choice)#THIS METHOD USED TO SEPARATE THE LETTER BY LETTER
        CONCATENATED_VARIABLE = player1choice_first_character[0]+player1choice_second_character[0]#STRING CONCATENTATION PURPOSE
    
        if (("rs" == CONCATENATED_VARIABLE) or ("pr" == CONCATENATED_VARIABLE) or ("ps" == CONCATENATED_VARIABLE) or ("sp" == CONCATENATED_VARIABLE)):
            print("Player 1 is the winner")
        else:
            print("Player 2 is the winner")

player1choice = str(input("Enter the choice 1"))
player2choice = str(input("Enter the choice 2"))
(check_status_two_players(player1choice,player2choice)) 
