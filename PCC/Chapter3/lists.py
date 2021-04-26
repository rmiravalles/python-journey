# A list is a collection of items in a particular order.
# Lists can contain any datatype.
# The elements of a list are enclosed in square brackets [] and each element
# of the list is separated by a comma.
# Lists are ordered, changeable, and allow duplicate values.
# Other data structures are tuples, sets, and dictionaries.

bikes = ['trek', 'cannondale', 'giant', 'specialized']

print(bikes)

# The position of an item in a list is its index.
# Index positions start at 0.

print(bikes[0])  # this will print the first element of the list.
print(bikes[2].title())  # this will print the third element, and will capitalize it.

# We can also count backwards, starting at the last element of a list.
# Its index is -1

print(bikes[-1])  # this will print the last element of the list.
print(bikes[-2])  # this will print the element before the last.

# Using individual elements from a list.

message = f"My first bicycle was a {bikes[2].title()}.\nNow I own a {bikes[0].title()}."
print(message)

# Lists are dynamic, meaning we can change them, by adding, removing or replacing elements.

cars = ['Ford', 'Citroen', 'Volvo', 'Fiat']

print(cars)

cars[0] = 'Mercedes'  # this will replace the first item in the list with this new item.
print(cars)

cars.append('BMW')  # this will add a new element to the end of the list.
cars.insert(1, 'Jaguar')  # this will insert a new element at position 1. all the elements after it will move to the right.

print(cars)

del cars[2]  # this will delete position 2 from the list.

print(cars)

new_car = cars.pop()  # the pop() method removes the last item from the list, but doesn't delete it permanently. here we're storing it in a new variable.

print(cars)
print(f"My new car is a {new_car}.")

first_car = cars.pop(1)  # here, we're popping from the list the item with index 1.

print(cars)
print(f"My first car was a {first_car}")

# We can remove an item from a list by calling its name.
# If there is more than one item with the same value, only the first occurrence will be removed.

cars.remove('Volvo')

print(cars)

# Sorting the elements of a list.

countries = ['Russia', 'France', 'Congo', 'Argentina', 'Nigeria', 'India']

print(countries)

countries.sort()  # this will sort the list alphabetically.

print(countries)

countries.sort(reverse=True)  # this will sort the list in reverse alphabetical order.

print(countries)

# Once we apply the sort method, the list will forever remain in this new order.
# We can use the sorted function to temporarily display the items of a list in a sorted order.

print("The list of countries in a reverse alphabetical order: ")
print(countries)
print("Now presented alphabetically:")
print(sorted(countries))
print("And here's the original list:")
print(countries)

# To find the length of a list, we use the len() function.

cities = ['Madrid', 'Moscow', 'London', 'Rome', 'Cairo', 'Tokyo']

print(cities)
print(len(cities))