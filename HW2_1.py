Eleks = ['John', 'Mary', 'Anna', 'Max', 'Igor', 'Serhii', 'Oleksandr']
Toshiba = ['John', 'Max', 'Oksana', 'Sasha', 'Anna', 'Alex', 'Nikolai']

Toshiba.extend(Eleks)
Eleks.clear()
print('Toshiba employees:', Toshiba)
print('Eleks employees:', Eleks)
