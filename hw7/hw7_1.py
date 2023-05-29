import sys


def custom_print(*args, sep=' ', end='\n', file=sys.stdout):
    text = sep.join(str(arg) for arg in args) + end
    file.write(text)


if __name__ == '__main__':
    custom_print('Hello, World!')

