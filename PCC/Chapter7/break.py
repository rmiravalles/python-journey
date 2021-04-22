# We use the break statement to exit a while loop without running any remaining code in the loop,
# regardless of the results of any conditional test.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

# A loop that starts with while True will run forever unless it reaches a break statement
# Here, the loop will keep running until the user enters 'quit', causing the program to exit the loop.
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")