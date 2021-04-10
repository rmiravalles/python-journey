# Checking whether new users have unique usernames, not in use by current users.

current_users = ['Bob', 'Raul', 'Sonia', 'Mike', 'Joe', 'Amir', 'Chris']
new_users = ['Tony', 'Sonia', 'Lucas', 'Bob', 'Alison', 'Nina', ' Ivan']

for new_user in new_users:
    if new_user in current_users:
        print("Please choose a different username.")
    else:
        print(f"User {new_user} created successfully!")