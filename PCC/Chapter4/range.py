# Python's range() function makes it easy to generate a series of numbers.

for value in range(1, 6):
    print(value)

# Here, Python will print the numbers 1 to 5.
# Python starts counting at the first value of the range and stops when it reaches the second value, 
# but it won't include it in the count.

# When there is only one argument in range, it will start the sequence of numbers at 0.
for value in range(8):
    print(value)

# We can convert a range of numbers into a list using the list() function.

numbers = list(range(1, 6))
print(numbers)

# We can tell Python to skip numbers in a given range by passing a third argument, which will represent the step size.
# Here Python will start counting at 2, skipping 2, until it reaches 10.
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# We can find the minimum, maximum and the sum of a list of numbers using the min(), max(), and sum() functions.
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))