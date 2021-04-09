# We can use for loops to print each item of a list.

colors = ['yellow', 'green', 'blue', 'pink', 'red', 'orange', 'magenta']

for color in colors:  # this means retrieve the first item of the list colors and associate it with a variable called color
    print(color)  # Python will execute this action with every element in the list, in order, until the list ends.

# We can choose any name we want for the temporary variable that will be associated with each value of the list.
# The set of steps in a for loop is repeated once for every item in the list.

# We can write as many lines of code as we want inside a for loop.
# Every indented line below for color in colors will be considered part of the loop.
# Any line of code after the for loop that are not indented are executed once.

for color in colors:
    print(f"{color.title()} is my favorite color.")
    print(f"That's why I painted my house {color}.\n")

print("What is your favorite color?")

# Python uses indentation to determine how a line or group of lines is related to the rest of the program.