# Here, the user will determine when to stop the while loop by entering a pre-defined value.

prompt = "\nTell me something, and I'll repeat it back to you: "
prompt += "\nEnter 'quit' to end the program"

message = ""  # we start with an empty message, so that the program has something to check when the loop starts

while message != "quit":
    message = input(prompt)
    print(message)
