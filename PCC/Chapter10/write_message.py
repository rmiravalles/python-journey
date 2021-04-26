# Writing to an empty file

filename = 'programming.txt'

# The open function here has two arguments: the name of the file and 'w', that tells Python we want
# to open the file in write mode. If the file doesn't exist already, Python creates it.
# If the file exists already, Python will erase all the contents in it before returning the file object.
# Other modes are:
# 'r': read mode.
# 'a': append mode.
# 'r+': read and write mode.

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("Python is my favorite language.\n")  # if we don't include newline (\n), Python will write everything on the same line.

# Python can only write strings to a text file.
