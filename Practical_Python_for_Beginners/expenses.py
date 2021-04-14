# A for loop to calculate the sum of all our expenses.

expenses = [10.50, 8, 5, 15, 20, 5, 3]
# sum = 0

# for x in expenses:
    # sum = sum + x

# print(f"You spent ${sum}.")

# A more concise way to do it.

total = sum(expenses)

print(f"You spent ${total}.")

# We can ask the user to input the expenses and in the end sum the total.

expenses2 = []  # we start with an empty list
num_expenses = int(input("Please enter the number of expenses: "))

for i in range(num_expenses):  # we'll perform the action as many times as the user entered above
    expenses2.append(float(input("Please enter an expense: ")))  # this will append the user's input as a new item to the list

total2 = sum(expenses2)  # here we'll store the sum of all items in expenses2 as a variable

print(f"You spent ${total2}.")
