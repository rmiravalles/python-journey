# A rock, paper, scissors game that we play against the computer

import random

computer_choice = random.choice(['scissors', 'paper', 'rock'])

user_choice = input("Do you want: rock, paper or scissors?\n")

if computer_choice == user_choice:
    print("That was a TIE!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(f"Congratulations! You WON! The computer had {computer_choice}.")
elif user_choice == 'paper' and computer_choice == 'rock':
    print(f"Congratulations! You WON! The computer had {computer_choice}.")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print(f"Congratulations! You WON! The computer had {computer_choice}.")
else:
    print("You lost  :( The comouter won this time  :D")