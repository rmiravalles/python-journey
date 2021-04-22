# For a program that should run only as long as many conditions are true, we can define one variable that
# determines whether or not the entire program is active. This variable is called a flag.
# It usually acts as a boolean variable indicating a condition to be true or false.
# Like that, the while statement needs to check only one condition: whether or not it's True (or False).

prompt = "\nTell me something, and I'll repeat it back to you: "
prompt += "\nEnter 'quit' or 'end' to end the program.\n"

active = True  # this is our flag, and it's set to True, so that the program starts in an active state

while active:  # as long as the active variable remains True, the loop will continue running
    message = input(prompt)

    if message == 'quit':  # if the user enters quit, we set the variable to False, therefore ending the program
        active = False
    
    elif message == 'end':  # with the flag, it's easier to add more conditions, as we just need to set them to False
        active = False
    
    else:  # if the user enters anything other than quit or end, we print the message
        print(message)
