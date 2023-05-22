def remove_vowels(input_string):
    vowels = "aeiouyAEIOUY"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result


input_str = "My name is Hlib! But you can call me Bread."
result = remove_vowels(input_str)
print("Original string:", input_str)
print("String with vowels removed:", result)
