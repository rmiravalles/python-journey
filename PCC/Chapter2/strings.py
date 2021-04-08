# A string is a data type. It is a series of characters wrapped around quotes.
# In Python, they can be ' or ".

print('I told everybody, "this is is the year of the Python!"')
print("Python's beauty is its flexibility.")

# Methods are used to modify an object.
# Format: object_name.method_name()

name = "billy bob thornton"
my_name = "roDRiGo MiRaVAlLEs dIAs"

print(name.title())  # this method capitalizes the first letter of each word inside the string
print(my_name.upper())  # this changes all the letters to uppercase
print(my_name.lower())  # this changes all the letters to lowercase

# f strings, or format strings, lets us use variables inside strings.
# The variable will be placed in the string inside curly brackets.

first_name = "john"
last_name = "coltrane"

print(f"{first_name} {last_name} is the greatest musician in history.")
print(f"{first_name.title()} {last_name.title()} is the greatest musician in history.")

full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"

print(message)
print()

# Adding whitespace

print("Python rules!")
print()
print("\tPython rules!")  # \t adds a tab before the beginning of the string
print()
print("Languages: \nPython\nJavaScript\nGo\nPerl")  # \n adds a new line

# Removing whitespace

language = "   Python   "

print(language)

print()
print(f"{language.rstrip()} is my favorite language")  # this will remove whitespace from the right of the string
print()
print(f"{language.lstrip()} is my favorite language")  # this will remove whitespace from the left of the string
print()
print(f"{language.strip()} is my favorite language")  # this will remove whitespace fom both sides