# An if statement allows us to examine the current condition of a program and respond appropriately to that condition.
# At the heart of every if statement is an expression that can be evaluated as true or false (a conditional test).
# If a conditional test evaluates to true, Python executes the code following the if statement.
# If the test evaluates to false, Python ignores the code following the if statement.
# If statements use indentation, like in for loops.

age = 19
if age >= 18:  # at this point, Python will check whether this is true, and if it is, it will move on to the next line
    print("You are old enough to vote!")

# In the case above, if age is less than 18, the program will produce no output.

# If we want to execute an action when a condition test passes and a different action if it doesn't, we use an if-else statement.
# The if-else is used when there are only two possible situations to evaluate.
# Below, the person is either old enough to vote or isn't old enough.

age2 = 17
if age2 >= 18:  # if this condition is true, print this, and if not, move to the else block
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# To test more than two conditions, we use the if-elif-else syntax.
# We can use as many elif blocks as we like.
# Let's consider an amusement park that charges different rates for different age groups.
# Admission for anyone under the age of 4 is free.
# Admission for anyone between the ages of 4 and 18 is $25.
# Admission for anyone between the ages of 18 and 65 is $40.
# Admission for anyone older than 65 is $20.

age3 = 12

if age3 < 4:
    print("Free of charge!")
elif age3 < 18:
    print("Admission price is $25.")
elif age3 < 65:
    print("Admission price is $40.")
else:
    print("Admission price is $20.")

print("Welcome to our park!")

# A more concise way to do it.
age4 = 70

if age4 < 4:
    price = 0
elif age4 < 18:
    price = 25
elif age4 < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

# We can ommit the else block at the end of an if-elif chain and use just elif blocks
# to make our conditions clearer.
age5 = 3

if age5 < 4:
    price = 0
elif age5 < 18:
    price = 25
elif age5 < 65:
    price = 40
elif age5 >= 65:  # here, we state the condition to be met, which makes it clearer
    price = 20

print(f"Your admission cost is ${price}.")

# To check multiple conditions, we use a series of if statements, with no elif or else blocks.
# This is used when more than one condition could be true and we want to act on every true condition.
toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in toppings:
    print("Adding mushrooms.")
if 'pepperoni' in toppings:
    print("Adding pepperoni.")
if 'extra cheese' in toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
