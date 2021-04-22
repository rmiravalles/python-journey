# Determining if a number is even or odd.

number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

if number % 2 == 0:  ## % is the modulo operator, it returns the remainder of the division.
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
