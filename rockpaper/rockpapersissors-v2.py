#!/usr/bin/env python3
import random
#Rock Paper Scissors Game
#Rock beats scissors, scissors beats paper, and paper beats rock. If both players choose the same action, the game is a tie.

print("Lets play a game.")
print("Pick your hand")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

player = int(input("Enter your hand (1-3): "))

computer_choice = random.randint(1,3)

#loop and print choices
if player == 1:
  print("You picked Rock")
elif player == 2:
  print("You picked Paper")
elif player == 3:
  print("You picked Scissors")
else:
  print("Invalid choice. Try again.")

if computer_choice == 1:
  print("Computer picked Rock")
elif computer_choice == 2:
  print("Computer picked Paper")
elif computer_choice == 3:
  print("Computer picked Scissors ")
else:
  print("Invalid choice. Try again.")

#loop for win 
if player == 1 and computer_choice == 1:
  print("It's a tie!")
elif player == 1 and computer_choice == 2:
  print("Computer wins!")
elif player == 1 and computer_choice == 3:
  print("You win!")

if player == 2 and computer_choice == 2:
  print("It's a tie!")
elif player == 2 and computer_choice == 3:
  print("Computer wins")
elif player == 2 and computer_choice == 1:
  print("You win")

if player == 3 and computer_choice == 3:
  print("It's a tie")
elif player == 3 and computer_choice == 2:
  print("You win")
elif player == 3 and computer_choice == 1:
  print("Computer wins")

