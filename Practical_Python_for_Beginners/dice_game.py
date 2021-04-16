# A dice rolling game for two players.

import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total


player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")

roll1 = roll_dice()
roll2 = roll_dice()

print(f"{player1} rolled {roll1}.")
print(f"{player2} rolled {roll2}.")

if roll1 > roll2:
    print(f"{player1} wins!")
elif roll2 > roll1:
    print(f"{player2} wins!")
else:
    print("That's a tie!")


