# Functions are blocks of code designed to perform a particular task.
# When we want to perform that task, we call the function, without the need to rewrite all the code.

# A function always starts with def followed by the name of the function.
# Inside the parenthesis goes the parameters the function needs to perform its job.
def greet_user():
    """Displays a simple greeting."""  # this is a docstring, a short description of what the function does
    print("Hello!")  # this is the actual task the function needs to perform


greet_user()  # to call the function, we type the function's name followed by parenthesis.


# Passing information to a Function.
def greeting(name):  # the variable name is called a parameter
    """Displays a simple greeting."""
    print(f"Hello, {name}!")


greeting('Joe')  # the value Joe is called an argument


# A Function can have more than one parameter

# Positional arguments
def my_pet(animal, name):
    """Displays information about a pet."""
    print(f"\nI have a {animal}.")
    print(f"My {animal}'s name is {name}.")


my_pet('cat', 'Billy')  # we must pass the arguments in the same order as they appear in the parameters

# Alternatively, we can use keyword arguments, where we directly associate the name and the value within the argument.
# Like that, the order in which the arguments appear doesn't matter.
my_pet(animal='horse', name='Phantom')
my_pet(name='Zeus', animal='rabbit')


# We can define default values for our parameters.
# If no argument is provided, Python will use the default value.

# parameters with default values need to be listed after all others that don't have default values
def pet(pet_name,
        animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


pet('Roger')
pet('Akira', 'lion')
