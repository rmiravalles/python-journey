# A list comprehension combines the for loop and the creation of new elements into one line,
# and automatically appends each new element.

squares = []  # we can start with an empty list
for value in range(1, 11):  # here we tell Python to loop through each value from 1 to 10
    square = value ** 2  # the current value is raised to the second power and assigned to the variable square
    squares.append(square)  # each new value of square is appended to the list squares

print(squares)  # finally, we print the list after the loop has finished running

# The same result from above can be achieved in a single line, with list comprehension.
squares_new = [value**2 for value in range(1, 11)]
print(squares_new)