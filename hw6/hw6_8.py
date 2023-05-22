def display_box(width: int, height: int, character: str = "*"):
    horizontal_line = character * width

    print(horizontal_line)
    for _ in range(height - 2):
        middle_line = character + " " * (width - 2) + character
        print(middle_line)
    print(horizontal_line)


display_box(5, 4, "x")
