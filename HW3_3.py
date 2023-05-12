friends = ['John', 'Marta', 'James']
enemies = ['John', 'Johnatan', 'Artur']

for friend in friends:
    if friend in enemies:
        print(f'{friend} we are not friends anymore')
    elif friend == 'James':
        continue
    else:
        print(f'{friend} we are best friends')
