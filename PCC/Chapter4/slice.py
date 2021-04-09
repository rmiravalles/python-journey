# Lists support the slice notation that allows us to get a sublist from a list.
# To make a slice, we specify the index of the first and last elements we want to work with.
# As with the range() function, Python stops one item before the second index.

# This will print a slice of the fruits list, from index 1 (the second element, apple) to index 3 (the fourth element).
# It won't include index 4 (orange)
fruits = ['banana', 'apple', 'watermelon', 'grape', 'orange', 'blueberry']
print(fruits[1:4])

# If you omit the first index, Python starts the slice at the beginning of the list.
print(fruits[:3])  

# If you set just the starting index, Python returns all items from the starting index to the end of the list.
print(fruits[2:])  

# We can use a slice in a for loop.
print('I eat these fruits every day:')
for fruit in fruits[:2]:
    print(fruit)
