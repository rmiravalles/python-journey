# A glossary of Python terms

glossary = {
    "dictionary": "an associative array that holds key-value pairs",
    "f-string": "a formatted string literal",
    "function": "a parametrized sequence of statements",
    "list": "a built-in Python sequence, can contain mixed types",
    "method": "a function which is called inside a class body",
    }

for term, definition in glossary.items():
    print(f"In Python, a {term} is {definition}.\n")

for term, definition in glossary.items():
    print(term, definition, sep=' : ')