def custom_map(callback, sequence):
    return [callback(item) for item in sequence]


def square_number(number):
    return number ** 2


if __name__ == '__main__':

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    squared_numbers = custom_map(square_number, numbers)

    print(squared_numbers)
