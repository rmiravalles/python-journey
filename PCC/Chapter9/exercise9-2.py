# Creating a Restaurant class and calling 3 different instances.

class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        print(f"{self.name} is a restaurant specializing in {self.type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant_a = Restaurant("Gino's", "Italian")
restaurant_b = Restaurant("Azumi", "Japanese")
restaurant_c = Restaurant("Mon Amour", "French")

restaurant_a.describe_restaurant()
restaurant_b.describe_restaurant()
restaurant_c.describe_restaurant()


