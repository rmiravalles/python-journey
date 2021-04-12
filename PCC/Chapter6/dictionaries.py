# A dictionary in Python is a collection of key-value pairs.
# Each key is connected to a value.
# A key's value can be a number, a string, a ñist, or another dictionary.
# A dictionary is wrapped in braces {}. Every key is connected to its value by a colon :
# and individual key-value pairs are separated by commas ,

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])  # this will get us the value associated with the color key from the alien_0 dictionary

# To get a value from the dictionary.

print(alien_0['color'])

new_points = alien_0['points']

print(f"You just earned {new_points} points!")

# Dictionaries are dynamic structures, meaning we can add, replace or remove key-value pairs.

alien_0['x_position'] = 0  # here we're adding new key-value pairs
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'  # here we're replacing an existing value with a new one
print(alien_0)

del alien_0['points']
print(alien_0)

# We can write a dictionary like this:

favorite_languages = {
    'Bob': 'Python',
    'Sarah': 'C',
    'Joe': 'Ruby',
    'Mel': 'Python',  # it is common practice to put a comma after the last key-value pair
    }

language = favorite_languages['Mel']
print(f"Mel's favorite programming language is {language}.")

# Using the get() method to return a value if the requested key doesn't exist:
alien_1 = {'color': 'blue', 'speed': 'slow'}

point_value = alien_1.get('points', 'No point value assigned.')
# if the 'points' key doesn't exist in the alien_1 dictionary, the program will
# return 'No point value assigned'.
