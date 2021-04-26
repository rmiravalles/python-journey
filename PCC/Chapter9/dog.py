# Introduction to Classes

class Dog:  # by convention, we use Capitalized names for classes
    """A simple attempt to model a dog."""  # a docstring with a description of what the class does

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

        