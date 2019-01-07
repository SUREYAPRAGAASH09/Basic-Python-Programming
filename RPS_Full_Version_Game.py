#this is full version means that user have the choice to get into boot Mode or Dual Player mode
import RPS_rounds_boot_gameUV
import RPS_rounds_dual_player_gameUV

def modeSelection():
    check = 1
    while(check):
        print("=========================================================================================================================================")
        print("\t\t\t\t\t\tThis Paper Scissors Rock Game")
        print("==========================================================================================================================================")
        print("\t\t*******Users can select any one of the mode to play**********************")
        print("\t\t\t\t\t1.Boot Mode")
        print("\t\t\t\t\t2.Dual Player Mode")
        Mode = int(input("Enter any of the mode to play the game \n \t\t\t\tEnter here ... "))
        count_variable = int(input("Enter how many ronuds do you want to play the game \n\t\t\tEnter here"))
        if (Mode == 1):
            RPS_rounds_boot_gameUV.count(count_variable)
        elif(Mode == 2):
            RPS_rounds_dual_player_gameUV.count(count_variable)
        else:
            print("Enter the correct Mode number to play the game")
        
        print("\n\t\tIf You want to continue the game Press 1\n\t\tPress 0 to discontinue the game")
        check = int(input("\nDo you like to continue to play the game"))
        

modeSelection()