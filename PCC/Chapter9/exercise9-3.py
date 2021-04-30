# A class to define a user's details.

class User:
    def __init__(self, first_name, last_name, user_id, email):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.email = email
    
    def describe_user(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nUser ID: {self.user_id}\nEmail: {self.email}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! Welcome to the Matrix!")

user_a = User("Michael", "Knight", 689, "mknight@mail.com")

user_a.describe_user()
user_a.greet_user()
