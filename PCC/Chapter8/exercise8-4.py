# Using default values.

def make_shirt(size="L", text="I love Python"):
    print(f"The size of my shirt is {size}.")
    print(f"And it's written {text} on it.")

make_shirt()
make_shirt("M", "Be Happy!")
make_shirt(text="Peace and Love", size="L")