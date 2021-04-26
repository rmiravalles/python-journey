# A simple game to guess the number.

import random

secret_number = random.randint(1,20)

print('I am thinking of a number between 1 and 20. Can you guess it?')
print('You have 6 chances to guess the number I am thinking of.')

for guesses in range(1,7):
    guess = int(input('Take a guess. '))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break

if guess == secret_number:
    print(f'Good job! You guessed my number in {guesses} guesses!')
else:
    print(f'Sorry. The number I was thinking of was {secret_number}')