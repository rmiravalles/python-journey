# We can combine lists and if statements to watch for special values inside a list.
# that need to be treated different than the other items of the list.

toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {topping}.")

print("\nYour pizza is ready!")

# We can have two lists, and check against both.
# The values in one list are checked against the other before the program proceeds.

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nYour pizza is ready!")