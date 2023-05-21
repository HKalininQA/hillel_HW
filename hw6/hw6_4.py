import re


def remove_numbers_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        updated_lines = []
        for line in lines:
            updated_line = re.sub(r'\d+', '', line)
            updated_lines.append(updated_line)

        with open(file_name, 'w') as file:
            file.writelines(updated_lines)

        print("Numbers have been removed from the file.")

    except FileNotFoundError:
        print("File not found.")
