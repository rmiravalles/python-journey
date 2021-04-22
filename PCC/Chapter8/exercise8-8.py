# Creating a dictionary from the user's input.

def make_album(title, artist):
    """Returns a dictionary with artist and album name"""
    album = {'title': title, 'artist': artist}
    return album

while True:
    print("\nPlease list your favorite music albums")
    print("Enter 'end' when you're done.")

    a_title = input("Album title: ")
    if a_title == 'end':
        break

    a_artist = input("Artist name: ")
    if a_artist == 'end':
        break

    album = make_album(a_title, a_artist)
    print(album)
