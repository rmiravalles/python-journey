# A contacts catalogue

contacts = {
    'number': 4,
    'students':
    [
        {'name': 'Bob Dylan', 'email': 'bdylan@example.com'},
        {'name': 'Miles Davis', 'email': 'mdavis@example.com'},
        {'name': 'Charlie Parker', 'email': 'cparker@example.com'},
        {'name': 'Bill Evans', 'email': 'bevans@example.com'},
    ]
}

for student in contacts['students']:
    print(student['email'])
