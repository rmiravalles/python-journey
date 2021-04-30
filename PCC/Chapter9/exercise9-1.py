# Creating a Restaurant class

class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        print(f"{self.name} is a restaurant specializing in {self.type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant = Restaurant("Gino's", "Italian")

print(f"{restaurant.name} is a new restaurant.")
print(f"{restaurant.name} serves {restaurant.type} food.")

restaurant.describe_restaurant()

restaurant.open_restaurant()

        