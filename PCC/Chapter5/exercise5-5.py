#The Alien Shooting Game

# A test that passes the condition.
alien_color = 'green'

if alien_color == 'green':
    print("Good shot! Yow just won 5 points!")

# A test that fails the condition.
alien_new_color = 'yellow'

if alien_new_color == 'green':
    print("Good shot! You just won 5 points!")

# if-else chain
alien_another_color = 'red'

if alien_another_color == 'green':
    print("You just shot a green alien! You won 5 points!")
elif alien_another_color == 'yellow':
    print("You just shot a yellow alien! You won 10 points!!")
else:
    print("You just shot a red alien! You won 15 points!!")


print("Thank you for playing!")



