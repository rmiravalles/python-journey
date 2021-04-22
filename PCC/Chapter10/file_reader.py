# The open function opens a file, and it takes one argument: the name of the file to be opened.
# The with block tells Python to close the file once all the processes inside its block finish
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)