file_path = 'test/data/data.txt'
with open(file_path, 'r') as file:
    for line in file:
        elements = line.strip().split()
        left_operand = int(elements[0])
        right_operand = int(elements[1])
        operation = int(elements[2])

        result = None
        if operation == 1:
            result = left_operand + right_operand
        elif operation == 2:
            result = left_operand - right_operand
        elif operation == 3:
            result = left_operand * right_operand

        if result is not None:
            print(result)
