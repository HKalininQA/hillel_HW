def print_function_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Function '{}' called. Result: {}".format(func.__name__, result))
        return result
    return wrapper


@print_function_name
def addition(a, b):
    return a + b


@print_function_name
def multiplication(a, b):
    return a * b


if __name__ == '__main__':
    print(addition(2, 3))
    print(multiplication(4, 5))
