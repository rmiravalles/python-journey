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

# To test more than two conditions, we the if-elif-else syntax.
# Let's consider an amusement park that charges different rates for different age groups.
# Admission for anyone under the age of 4 is free.
# Admission for anyone between the ages of 4 and 18 is $25.
# Admission for anyone age 18 or older is $40.

age3 = 12
if age3 < 4:
    print("Free of charge!")
elif age3 < 18:
    print("Admission price is $25.")
else:
    print("Admission price is $40.")

print("Welcome to our park!")

# A more concise way to do it.
age4 = 21
if age4 < 4:
    price = 0
elif age4 < 18:
    price = 25
else:
    price = 40

   print(f"Your admission cost is ${price}.")
