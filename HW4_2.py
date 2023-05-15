import re
list_camel = ["FirstItem", "FriendsList", "MyTuple"]
convert = ' '.join(list_camel)
convert = re.sub('([a-z0-9])([A-Z])', r'\1_\2', convert).lower()
list_snake = convert.split(" ")
print(list_snake)


