filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  # the readlines method takes each line from the file and stores them in a list.

for line in lines:
    print(line.rstrip())

# Here we'll build a single string from the file, that ahd had separate lines.

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

