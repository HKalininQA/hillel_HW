eleks = ['John', 'Mary', 'Anna', 'Max', 'Igor', 'Serhii', 'Oleksandr']
toshiba = ['John', 'Max', 'Oksana', 'Sasha', 'Anna', 'Alex', 'Nikolai']

toshiba.extend(eleks)
eleks.clear()
print('Toshiba employees:', toshiba)
print('Eleks employees:', eleks)
