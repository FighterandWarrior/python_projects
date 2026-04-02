#!usr/bin/python3

#Rock smashes scissors
#paper covers rock 
#scissors cut paper

#1.take user input
#2.make the computer choose
#3.determine a winner
#4.play/run several games in a row 

import random

while True:
        
    user_action = input("Pick a choice (rock, paper, scissors): ")

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\n You chose {user_action}, computer chose {computer_action}.\n\n")

    if user_action == computer_action:
        print(f"Both selected {user_action}. It's a tie.")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
            
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break