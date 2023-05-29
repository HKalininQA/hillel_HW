def generate_even_squares():
    num = 0
    while num <= 1000000000:
        yield num ** 2
        num += 2

# Testing the generator function
for square in generate_even_squares():
    print(square)
