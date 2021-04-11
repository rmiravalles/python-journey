# An age calculator that will output our age in decades and years.

# Here, we are using two built-in functions:
# int converts a value to an integer number.
# input asks for the user input

age = int(input("How old are you?\n"))

decades = age // 10  # this is a floor division; it discards the decimal points of the result
years = age % 10  # this is a modulus division; it returns the remainder of the division

print(f"You are {decades} decades and {years} years old.")