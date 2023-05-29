def custom_filter(callback, sequence):
    return [item for item in sequence if callback(item)]


def starts_with_m(string):
    return string.startswith('M')


if __name__ == '__main__':
    names = ['John', 'Mary', 'Mark', 'Lucy', 'Hamish', 'Mannie']
    filtered_names = custom_filter(starts_with_m, names)

    print(filtered_names)
