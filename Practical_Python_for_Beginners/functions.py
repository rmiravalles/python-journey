# Functions are like mini-programs that execute a specific task.
# Functions are reusable.
# Functions allow us to organize our code by logical units.

def greeting(name):  # name is a variable that exists only inside the function where it was defined (local scope)
    print('Hello', name)

input_name = input("Please enter your name:\n")

greeting(input_name)  # the function just runs if we call it

print(f"Thanks {input_name}.")

# A function that adds two numbers and returns the result.

def addition(a, b):
    return a + b

# this is the main program
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

result = addition(num1, num2)
print(f"The result is {result}.")