# The open function opens a file, and it takes one argument: the name of the file to be opened.
# The open function returns an object representing the object.
# In the example below, this object is represented by file_object.
# The with block tells Python to close the file once all the processes inside its block finish.
# When using with, the file object returned by open will be available only inside the with block.

filename = 'pi_digits.txt'  # it's common convention when working with a file to assign it to a variable

with open(filename) as file_object:
    contents = file_object.read()  # the read method reads the entire contents of the file

print(contents.rstrip())  # the rstrip method removes any white space from the right side of the string