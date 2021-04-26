# Writing several names to a text file using a while loop.

filename = 'guest_book.txt'

print("Enter 'quit' when you're done.")

while True:
    guest = input("\nWhat is your name? ")
    if guest == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{guest}\n")
        print(f"Hi {guest}, you have been added to the guest book.")


