# Tuples, like lists, are used to store multiple items in a single variable.
# Tuples are immutable, meaning we can't change its values.
# Tuples are written around parenthesis ().
# We can use tuples to store sets of values that should not be changed throughout the life of a program.

dimensions = (200, 140)
dimensions[0] = 250  # if we try to modify an element in a tuple, we get an error

# We can, however, assign new values to a tuple. This will redefine the entire tuple.
dimensions = (180, 110)