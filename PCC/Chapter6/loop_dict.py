# We can loop through a dictionary's key-value pairs, through its keys or through its values.

user_0 = {
    'username': 'bdylan',
    'first': 'Bob',
    'last': 'Dylan',
    }

# To loop through all key-value pairs, we use the items() method.
for key, value in user_0.items():  # key and value are the temp variables, and we can name them anything
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'Bob': 'Python',
    'Sarah': 'C',
    'Joe': 'Ruby',
    'Mel': 'Python',
    }

for name, language in favorite_languages.items():
    print(f"{name}'s favorite language is {language}.")

# To loop through all the keys, we use the keys() method.
for name in favorite_languages.keys():
    print(name)

# This wields the same result (looping through the keys is the default behavior).
for name in favorite_languages:
    print(name)

# Python will return the items ins the dictionary in the same order as they appear.
# To sort the result we can use the sorted() function.
for name in sorted(favorite_languages.keys()):
    print(f"{name}, thank you for participating in this poll!")

# To loop through the values we use the values() method.
for language in favorite_languages.values():
    print(language)

# The action above will output all the values in the dict, including repeated ones.
# To output just unique values, we use set().
for language in set(favorite_languages.values()):
    print(language)

# A set is a sequence of values wrapped around curly braces and separated by commas.
languages = {'Python', 'Ruby', 'Python', 'C', 'Java', 'Ruby'}

print(languages)


