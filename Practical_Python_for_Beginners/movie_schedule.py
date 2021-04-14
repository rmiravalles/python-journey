# A movie schedule stored in a dictionary.

current_movies = {
    'The Grinch': '11:00am',
    'Rudolph': '1:00pm',
    'Frosty the Snowman': '3:00pm',
    'Christmas Vacation': '5:00pm',
    }

print("We are currently showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie you would you like the showtime for?\n")

showtime = current_movies.get(movie)
if showtime is None:
    print("Sorry. This movie isn't playing.")
else:
    print(f"{movie} is playing at {showtime}.")