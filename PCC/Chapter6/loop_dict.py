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


