# We can make an argument optional.
# We can use default values to accomplish that.

def full_name(first, last, middle=''):  # we set middle name with the default value of an empty string
    """Returns a full name, properly formatted"""
    name = f"{first} {middle} {last}"
    return name.title()


actor = full_name('john', 'cleese')

print(actor)

# Since the middle name argument comes last, we need to ensure we pass the middle name argument last too.
musician = full_name('john', 'hooker', 'lee')

print(musician)
