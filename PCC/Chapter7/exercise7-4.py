# A program to enter pizza toppings.

prompt = "\nWelcome to Vito's Pizza! Please enter the ingredient for your pizza topping."
prompt += "\nWhen you're done choosing, please enter quit "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"{topping} added to your pizza!")
