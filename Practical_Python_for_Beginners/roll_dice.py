import random

roll = random.randint(1,6)

# print(f"The computer rolled a {roll}.")

guess = int(input("Try to guess the dice roll:\n"))

if guess == roll:
    print(f"Correct! The computer rolled a {roll}!")
else:
    print(f"Wrong! The computer rolled a {roll}!")
