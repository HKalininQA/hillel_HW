message = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
message = message.replace('=sssss', '&')
message = message.replace('&&', '&')
filtered_message = dict((key.strip(), (value.strip()))
                for key,value in (char.split('=')
                            for char in message.split('&')))
print(f'Person profile:{filtered_message}')
