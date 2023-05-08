omnivores = ['John', 'Mary', 'Anna', 'Mark']
vegetarians = ['Josef', 'Julia', 'Hamood', 'Habibi']
guests= []

#guests = [*omnivores, *vegetarians]

guests.extend(omnivores)
guests.extend(vegetarians)
print('List of guests who can eat vegetables and herbs:', guests)

