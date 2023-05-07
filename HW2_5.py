names = ['John Doe', 'John Dow', 'Mary Sued', 'Mark Sue', 'Max Doe', 'Mary Sued', 'John Doe', 'Bob Hill', 'Bob Hill']

names_unique = []

for name in names:
    if name not in names_unique:
        names_unique.append(name)

print(names_unique)
