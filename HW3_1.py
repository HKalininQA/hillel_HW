numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd = []
even = []

for index, number in enumerate(numbers):
    if index % 2 == 1 in numbers:
        odd.append((index, number))
    else:
       even.append((index, number))

print(f'List of numbers with odd index:{odd}')
print(f'List of numbers with even index:{even}')
