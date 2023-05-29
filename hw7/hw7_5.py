def custom_all(sequence):
    for item in sequence:
        if not item:
            return False
    return True


if __name__ == '__main__':
    sequence = [True, "Hello", 42, [1, 2, 3]]
    result = custom_all(sequence)
    print(result)
