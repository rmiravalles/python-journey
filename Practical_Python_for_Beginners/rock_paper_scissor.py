# A rock, paper, scissors game that we play against the computer

computer_choice = 'scissors'

user_choice = input("Do you want: rock, paper or scissors?\n")

if computer_choice == user_choice:
    print("That was a TIE!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("Congratulations! You WON!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("Congratulations! You WON!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("Congratulations! You WON!")
else:
    print("You lost  :( The comouter won this time  :D")