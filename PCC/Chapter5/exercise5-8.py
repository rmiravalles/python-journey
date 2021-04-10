# A unique welcome message to the admin.

usernames = ['Joe', 'Susan', 'admin', 'Pablo', 'Jane', 'Sandra']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}. Welcome!")
