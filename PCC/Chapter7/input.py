# The input() function lets the user enter data.
# The input() function takes one argument, the prompt, or instructions, that we want to display to the user.

name = input("Please enter your name: ")
print(f"Hello, {name}!")

# Writing a longer prompt, using a different approach.
message = "If you tell us who you are, we can personalize the messages you see on the screen."
message += "\nWhat is your name? "  # the += will add this new string to the end of the variable message

name2 = input(message)
print(f"Hello, {name2}!")

# By default, Python interprets the user's input as a string.
# We can use the int() function to convert the string into an integer or  float() to convert it into a float.

height = int(input("How tall are you in cm? "))

if height >= 120:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

