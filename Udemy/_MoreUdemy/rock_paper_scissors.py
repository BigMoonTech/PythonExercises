#improved random numbers 
from secrets import randbelow


player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print("...rock... \n...paper... \n...scissors...")

    #player variables
    player_1 = input("enter Player 1's choice: ").lower()
    computer = ""

    #random int from 0-2
    rand_num = randbelow(3)

    #set computer to rock, paper, or scissors based on random int
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer chooses {computer.upper()}.")

    while True:
        #check for invalid responses and empty strings
        if (player_1 != "rock") and (player_1 != "paper") and (player_1 != "scissors"):
            print("Player: Invalid choice.")
            break
        else:
            #check for draw
            if computer == player_1:
                print("Tie!")
            #computer win possibilities
            elif (player_1 == "rock" and computer == "paper") or (player_1 == "paper" and computer == "scissors") or (player_1 == "scissors" and computer == "rock"):
                computer_wins += 1
                print("The computer wins!")
            else:
                player_wins += 1
                print("Player 1 wins!")
            print(f"Scores: Player - {player_wins} Computer - {computer_wins}")
            break
