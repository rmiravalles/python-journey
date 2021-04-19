# We can move items between lists using while loops.

# Let's consider two lists of users, one for unconfirmed and the other for confirmed users.
# We'll move the users from the unconfirmed to the confirmed list.

unconfirmed_users = ['Alice', 'Joe', 'Ray', 'Wilson', 'Maggie', 'Julia']
confirmed_users = []  # we'll start with an empty list, and move the users from unconfirmed_users here.

# We'll now verify each user until there are no more unconfirmed users,
# And we'll move them to the confirmed_users list.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user {current_user}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")

for confirmed_user in confirmed_users:
    print(confirmed_user)
