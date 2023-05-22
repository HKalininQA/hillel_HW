import math


def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side

    return perimeter, area, diagonal


side_length = 3
perimeter, area, diagonal = square(side_length)

print("Perimeter:", perimeter)
print("Area:", area)
print("Diagonal:", diagonal)
