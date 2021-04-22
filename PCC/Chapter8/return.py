# A return value is a value that the function returns, after executing some processes.
# It takes a value from inside the function and sends it back to the line that called the function.

def full_name(first, last):  # this function takes first and last as parameters
    """Returns a full name, properly formatted"""
    name = f"{first} {last}"  # it combines the two parameters and assigns them to the name variable
    return name.title()  # the name is converted to title case and returned to the calling line


actor = full_name('john', 'cleese')

print(actor)


# Returning a dictionary

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('Ornette', 'Coleman')
print(musician)
