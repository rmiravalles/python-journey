# We'll check the weather and decide whether we should go outside or stay inside.

temperature = 95
forecast = "rain"

if temperature > 80:  # if this statement is true, do the following code block
    print("It's too hot!")
    print("Stay inside!")

# The line below is outside the code block; it'll run regardless of the above statement being true or false.
# If it's false, the program will run just this line.
print("Have a good day!")

# Using AND, OR, and NOT logical operators to combine multiple conditions.

if temperature > 80 or temperature < 60:
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")

# FALSE or FALSE == FALSE
# TRUE or TRUE == TRUE
# FALSE or TRUE == TRUE

if temperature < 90 and forecast != "rain":
    print("Go outside!")
else:
    print("Stay inside!")

# TRUE and FALSE == FALSE
# TRUE and TRUE == TRUE
# FALSE and FALSE == FALSE

# NOT logical operator

if not forecast == "rain":
    print("Go outside!")
else:
    print("Stay inside!")

# not TRUE == FALSE
# not FALSE == TRUE

# Boolean values: true, false

raining = True

if raining:
    print("Go outside!")
else:
    print("Stay inside!")

if not raining:  # this statement is false, since raining == true, and not true is false.
    print("Go outside!")
else:
    print("Stay inside!")


