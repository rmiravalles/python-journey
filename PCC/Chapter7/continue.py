# We use the continue statement to return to the beginning of the loop based on the result of a conditional test.

# This program will count from 1 to 10, but will print only the odd numbers in this range.
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # if the above condition is true, Python will ignore the code that follows and will return to the beginning.

    print(current_number)
