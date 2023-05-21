import os
import random

operations = [1, 2, 3]
tuples_list = []

for i in range(100):
    left_operand = random.randint(1, 100)
    right_operand = random.randint(1, 100)
    operation = random.choice(operations)
    tuples_list.append((left_operand, right_operand, operation))

directory = 'test/data'
os.makedirs(directory, exist_ok=True)

file_path = os.path.join(directory, 'data.txt')
with open(file_path, 'w') as file:
    for tuple_item in tuples_list:
        file.write(' '.join(map(str, tuple_item)) + '\n')
