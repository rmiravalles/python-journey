# A program that prompts the user for their name and stores the information in a text file.

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(input("What is your name? "))

