# Filling a dictionary with user input.

responses = {}  # we'll start with an empty dictionary, which we'll fill with the data gathered with the user inputs

# Here we'll use a flag
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What is your favorite movie? ")

    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name}'s favorite movie is {response}.")


