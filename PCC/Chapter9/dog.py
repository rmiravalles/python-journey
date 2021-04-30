# Introduction to Classes
# A class can be thought of as a set of instructions on how to make an instance (an object)

class Dog:  # by convention, we use Capitalized names for classes
    """A simple attempt to model a dog."""  # a docstring with a description of what the class does

    # functions that are part of a class are called methods
    # the __init__ method must be present, and it is called automatically when we create an instance
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Here we'll create an instance based on the Dog class
my_dog = Dog("Willie", 6)

# To access the attributes of an instance we use the dot notation.
# my_dog.name will retrieve the dog's name.
print(f"My dog's name is {my_dog.name}.")
print(f"{my_dog.name} is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Lucy", 4)

print(f"Your dog's name is {your_dog.name}.")
print(f"{your_dog.name} is {your_dog.age} years old.")

your_dog.sit()
your_dog.roll_over()



        