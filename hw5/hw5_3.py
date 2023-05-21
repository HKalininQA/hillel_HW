file_path = '../hw5/text.txt'
letter_count = {}

with open(file_path, 'r') as text:
    content = text.read()
    content = content.lower()

for let in content:
    if let.isalpha():
        if let in letter_count:
            letter_count[let] += 1
        else:
            letter_count[let] = 1

for letter, count in letter_count.items():
    print(f"{letter}: {count}")
