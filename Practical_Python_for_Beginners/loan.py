# A loan calculator that calculates how much of our loan we paid off after a given number of months.

# Get the loan details.
money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the annual percentage rate?\n"))  # 3% is the common
payment = float(input("What will your monthly payment be, in dollars?\n"))
months = int(input("How many months do you want to se the results for?\n"))

# Divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
    # Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed < 0):
        print(f"The last payment is {money_owed}.")
        print("You paid off the loan in", i+1, "months.")
        break  # this interrupts the current loop

    # Make payment
    money_owed = money_owed - payment

    # Print the results after this month
    print(f"Paid {payment}, of which {interest_paid} was interest.")
    print(f"Now I owe {money_owed}.")
