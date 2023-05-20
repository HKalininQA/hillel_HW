file_path = '../hw5/text.txt'
letter_count = {}

with open(file_path, 'r') as text:
    for line in text:
        for let in line:
            if let.isalpha():
                let = let.lower()
                if let in letter_count:
                    letter_count[let] += 1
                else:
                    letter_count[let] = 1

for letter, count in letter_count.items():
    print(f"{letter}: {count}")


