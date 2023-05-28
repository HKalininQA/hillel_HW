def custom_max(sequence, amount=1):
    return sorted(sequence)[-amount:]


def custom_min(sequence, amount=1):
    return sorted(sequence)[:amount]


if __name__ == '__main__':
    numbers = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(custom_max(numbers, 1))
    print(custom_min(numbers, 1))
