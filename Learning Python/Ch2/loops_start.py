#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  # while (x<5):
  #       print(x)
  #       x = x+1


  # define a for loop
  # for x in range(5,10):
  #       print(x)


  # use a for loop over a collection
  # days = ["Mon", "Thu", "Wed", "Thu", "Fri", "Sat", "Sun"]
  # for d in days:
  #       print(d)

  
  # use the break and continue statements
  for x in range(5,10):
        # if (x==7):break  # the break statement breaks the execution of a loop if a condition is met
        if (x % 2 == 0):continue  # if this is true, don't execute the rest of the loop and go back to the top
        print(x)


  # using the enumerate() function to get index 
  days = ["Mon", "Thu", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for i,d in enumerate(days):  # the enumerate function returns the index value of the items in the list
        print(i, d)
  
if __name__ == "__main__":
  main()
