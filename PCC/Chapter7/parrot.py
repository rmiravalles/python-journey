# Here, the user will determine when to stop the while loop by entering a pre-defined value.

prompt = "\nTell me something, and I'll repeat it back to you: "
prompt += "\nEnter 'quit' to end the program.\n"

message = ""  # we start with an empty message, so that the program has something to check when the loop starts

while message != "quit":  # until the value of the message variable is different than quit, the loop will keep running
    message = input(prompt)

    if message != 'quit':  # here we tell Python to print the message just if it's different than quit
        print(message)

